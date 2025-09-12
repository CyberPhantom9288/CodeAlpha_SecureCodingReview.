from tool.banner import show_banner
from tool.analyzer import analyze_code
from tool.report import generate_report

def main():
    show_banner()
    file_path = input("Enter the path of the code file to review: ").strip()

    try:
        with open(file_path, "r") as f:
            content = f.read()

        findings = analyze_code(content)
        generate_report(findings)

    except FileNotFoundError:
        print("[-] File not found! Please check the path.")

if __name__ == "__main__":
    main()
