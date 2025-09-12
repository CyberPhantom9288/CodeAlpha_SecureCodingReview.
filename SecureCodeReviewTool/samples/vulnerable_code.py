# 🚨 Vulnerable Example Code 🚨

# Hardcoded password
password = "admin123"

# User input without validation
user = input("Enter username: ")
pwd = input("Enter password: ")

# SQL query vulnerable to injection
query = "SELECT * FROM users WHERE user = '" + user + "' AND pwd = '" + pwd + "'"
print("Running query:", query)

# Dangerous eval usage
eval("print('Hello ' + user)")
