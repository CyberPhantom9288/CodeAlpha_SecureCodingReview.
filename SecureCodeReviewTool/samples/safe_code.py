# ✅ Secure Example Code ✅

import os
import sqlite3
import getpass

# Securely handle password input
user = input("Enter username: ").strip()
pwd = getpass.getpass("Enter password: ").strip()

# Secure query with parameterized statements
con = sqlite3.connect("users.db")
cur = con.cursor()
cur.execute("SELECT * FROM users WHERE user=? AND pwd=?", (user, pwd))

print("Secure query executed successfully")

# No eval(), no hardcoded credentials
