from analyzer import PhishingAnalyzer

def main():
    print("============================================================")
    print("     PHISHING EMAIL DETECTION SYSTEM ")
    print("============================================================")
    print()
    
    analyzer = PhishingAnalyzer()
    
    print(" Paste the email content here (press Enter twice to finish):")
    print("----------------------------------------------------------------------")
    
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    email_content = "\n".join(lines)
    
    if not email_content.strip():
        print("\n No content entered!")
        return
    
    print("\n" + "==================================================")
    print(" ANALYSIS RESULT:")
    print("=========================================================")
    
    result = analyzer.analyze(email_content)
    
    print(f"\n Risk Level: {result['risk_level']}")
    print(f" Suspicion Score: {result['score']}/100")
    print(f" Verdict: {result['verdict']}")
    print(f" Recommended Action: {result['action']}")
    
    if result['red_flags']:
        print("\n Red Flags Detected:")
        for flag in result['red_flags']:
            print(f"   {flag}")
    else:
        print("\n No red flags detected")
    
    print("\n" + "=======================================================")

if __name__ == "__main__":
    main()