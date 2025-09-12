import re

def analyze_code(file_content):
    findings = []

    # Hardcoded password
    if re.search(r"(password\s*=\s*['\"].+['\"])", file_content, re.IGNORECASE):
        findings.append({
            "issue": "Hardcoded password found",
            "recommendation": "Use environment variables or config files instead."
        })

    # SQL Injection
    if re.search(r"(SELECT\s+.*\s+FROM\s+.*\+.*)", file_content, re.IGNORECASE):
        findings.append({
            "issue": "Possible SQL Injection",
            "recommendation": "Use prepared statements / parameterized queries."
        })

    # Weak input validation
    if "input(" in file_content and not re.search(r"(strip|isdigit|isalpha)", file_content):
        findings.append({
            "issue": "Weak input validation",
            "recommendation": "Sanitize and validate all inputs."
        })

    # Dangerous eval()
    if "eval(" in file_content:
        findings.append({
            "issue": "Use of eval() detected",
            "recommendation": "Avoid eval(), use safer alternatives like ast.literal_eval."
        })

    return findings
