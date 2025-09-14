# 🔐 CodeAlpha_SecureCodingReview

A **Secure Coding Review Tool** built in Python for my CodeAlpha Internship.  
This tool scans Python source code, detects insecure coding patterns, and provides remediation suggestions based on secure coding practices.

---

## 🚀 Features
- Detects **common security issues** such as:
  - Hardcoded credentials
  - Insecure function usage (e.g., `eval`)
  - Missing input validation
  - Poor exception handling
- Generates a **security report**
- Example vulnerable & safe code included for testing
- Simple, extensible codebase (add your own rules in `tool/analyzer.py`)

---

## ⚙ Installation

1. Clone this repository:
   ```
   git clone https://github.com/CyberPhantom9288/CodeAlpha_SecureCodingReview.git
   cd CodeAlpha_NetworkPacketSniffer
    pip install -r requirements.txt
   python3 main.py
   ```

# Example Run

$ python3 main.py
======================================
🔐 Secure Code Review Tool
======================================

[+] Analyzing samples/vulnerable_code.py
[!] Hardcoded credentials found
[!] Insecure function usage: eval()

[+] Analyzing samples/safe_code.py
[✓] No critical issues found

✅ Report generated: report_output.txt
    
