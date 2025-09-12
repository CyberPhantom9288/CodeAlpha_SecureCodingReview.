# 🕵‍♂ CodeAlpha_NetworkPacketSniffer

A *network packet sniffer* built in Python using *Scapy* for my CodeAlpha Internship.  
This project captures live network traffic, analyzes packet structure, and displays key details like *source/destination IPs, protocols, ports, and payloads*.

---

## 🚀 Features
- Capture *real-time network packets*
- Analyze:
  - *Ethernet Layer* → MAC addresses
  - *IP Layer* → Source/Destination IPs, TTL, Protocol
  - *Transport Layer* → TCP/UDP/ICMP details
- Extract and display *payload data*
- Protocol-based *packet filtering*
- Educational tool to understand *how data flows through a network*

---

---

## ⚙ Installation

1. Clone this repository:
   ```
   git clone https://github.com/CyberPhantom9288/CodeAlpha_NetworkPacketSniffer.git
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
    
