
# 🚀 Automated Security Lab: SAST & Security Gate with Semgrep

This project demonstrates a **full DevSecOps workflow** to detect, analyze, and remediate critical vulnerabilities in a Python Flask application using **Semgrep**, automation scripts, and GitHub Actions pipelines. This lab showcases **secure coding practices, automated scanning, and CI/CD enforcement**.

---

## 1️⃣ Creation of a New Repository
- Initialized a **GitHub repository** to host the project.
- Configured development (`dev`) and main (`main`) branches.
- Ensured proper **version control and tracking** for all files.

---

## 2️⃣ Validation
- Verified repository setup.
- Prepared environment for Python and GitHub Actions.

---

## 3️⃣ Creation of `app.py`
- Developed a simple **Flask application**.
- Initially created **without vulnerabilities**, but prepared to simulate `debug=True` for SAST scanning.

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, secure world!"

# Safe debug mode via environment variable
import os
debug_mode = os.getenv('FLASK_DEBUG', '0') == '1'
app.run(debug=debug_mode)
````

---

## 4️⃣ Pipeline 01: SAST Scan with Semgrep

* Configured **GitHub Actions workflow** to perform a **Static Application Security Test (SAST)** using Semgrep.
* Scanned the Flask app for **critical vulnerabilities**.
* Generated **reports in TXT and JSON** formats.

---

## 5️⃣ Scan Report Pipeline 01: Vulnerability Detected

* Semgrep detected **`debug=True` in Flask**, a critical security misconfiguration.
* The **pipeline automatically stopped** and displayed **red** in GitHub Actions.
* Generated a **TXT report** for review.

---

## 6️⃣ TXT File Interpretation

* The Semgrep TXT report was analyzed using **ChatGPT**.
* Produced **actionable remediation recommendations** sent to supervisors.
* Streamlines **vulnerability understanding and reporting**.

---

## 7️⃣ Automatic Remediation Script

* Created a **Python script** to automatically remediate the vulnerability:

**Features:**

* Replaces `debug=True` with environment-controlled debug mode.
* Performs a **rescan** after remediation.
* Generates **logs in TXT** to confirm success.

```bash
python fix_and_rescan.py
# Generates: fix_rescan_log.txt + semgrep_output.txt
```

---

## 8️⃣ Pipeline 02: Security Gate

* Configured a **second GitHub Actions workflow** as a **Security Gate**.
* Ensures that **critical vulnerabilities block deployment**.
* Pipeline automatically turns **red** if vulnerabilities are detected.

**Key Features:**

* Scans **all Python files** in the repo.
* Generates **artifacts** (TXT and JSON reports) for review.
* Fails the pipeline (`exit 1`) if critical issues remain.

---

## 9️⃣ Outcome

* Demonstrated a **complete DevSecOps lifecycle**:

  1. Vulnerability detection (SAST scan)
  2. Automated remediation
  3. Rescan verification
  4. Pipeline enforcement (Security Gate)
* Highlights:

  * **Automation and efficiency** in securing applications
  * **Hands-on experience** with GitHub Actions, Semgrep, and Python
  * **Professional-grade workflow simulation**

---

## 1️⃣0️⃣ Key Takeaways for Recruiters

* Ability to **implement automated security scans** in CI/CD pipelines.
* Experience with **critical vulnerability detection and remediation**.
* Knowledge of **pipeline enforcement, artifact management, and reporting**.
* Strong **DevSecOps and SAST/Security Gate expertise**.

---

This project provides a **practical, hands-on demonstration** of automating vulnerability detection, remediation, and enforcement in real-world pipelines.

```

