import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_user_by_name(name):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # ❌ Vulnérabilité volontaire : injection SQL
    query = f"SELECT * FROM users WHERE name = '{name}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

@app.route("/user")
def user():
    name = request.args.get("name", "")
    data = get_user_by_name(name)
    return {"users": data}

if __name__ == "__main__":
    app.run(debug=True)
