import os
import subprocess
import re
from datetime import datetime

# ----- CONFIG -----
TARGET_FILE = "app.py"
BACKUP_FILE = "app_backup.py"
LOG_FILE = "fix_rescan_log.txt"
SEMgrep_RULES = "https://semgrep.dev/p/r/python.flask.security.audit.debug-enabled.debug-enabled"

# ----- Étape 0 : Préparer le log -----
def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)

write_log("----- DÉBUT DE L'OPÉRATION -----")

# ----- Étape 1 : Sauvegarde du fichier original -----
try:
    with open(TARGET_FILE, "r") as f:
        content = f.read()
    with open(BACKUP_FILE, "w") as f:
        f.write(content)
    write_log(f"[+] Sauvegarde effectuée : {BACKUP_FILE}")
except Exception as e:
    write_log(f"[❌] Erreur lors de la sauvegarde : {e}")
    exit(1)

# ----- Étape 2 : Remplacement automatique -----
try:
    new_content = re.sub(
        r"app\.run\s*\(\s*debug\s*=\s*True\s*\)",
        "import os\ndebug_mode = os.getenv('FLASK_DEBUG', '0') == '1'\napp.run(debug=debug_mode)",
        content
    )

    with open(TARGET_FILE, "w") as f:
        f.write(new_content)
    write_log("[+] Correction appliquée : debug=True remplacé par variable d'environnement")
except Exception as e:
    write_log(f"[❌] Erreur lors de la correction : {e}")
    exit(1)

# ----- Étape 3 : Lancer le scan Semgrep -----
write_log("[+] Lancement du scan Semgrep...")
try:
    result = subprocess.run(
        ["semgrep", "--config", SEMgrep_RULES, TARGET_FILE],
        capture_output=True,
        text=True,
        check=False
    )
    # Enregistrer le stdout complet pour info
    with open("semgrep_output.txt", "w") as f:
        f.write(result.stdout)
    
    # Vérifier si la vulnérabilité persiste
    if "debug-enabled" not in result.stdout:
        write_log("[✅] La vulnérabilité debug=True a été corrigée !")
        write_log("----- FIN DE L'OPÉRATION : SUCCESS -----\n")
    else:
        write_log("[⚠️] La vulnérabilité persiste, vérifier le fichier.")
        write_log("----- FIN DE L'OPÉRATION : FAILURE -----\n")
except FileNotFoundError:
    write_log("[❌] Semgrep n'est pas installé ou non trouvé dans le PATH.")
    write_log("----- FIN DE L'OPÉRATION : FAILURE -----\n")
except Exception as e:
    write_log(f"[❌] Erreur lors du scan Semgrep : {e}")
    write_log("----- FIN DE L'OPÉRATION : FAILURE -----\n")
