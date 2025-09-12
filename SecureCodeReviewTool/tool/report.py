def generate_report(findings):
    print("\n=== Secure Code Review Report ===\n")
    if not findings:
        print("[+] No major vulnerabilities detected. Code looks secure!")
    else:
        for idx, item in enumerate(findings, start=1):
            print(f"Issue {idx}: {item['issue']}")
            print(f"   Recommendation: {item['recommendation']}\n")
