markdown
# Phishing Awareness Analysis Project

A Python-based command-line tool that analyzes email content to detect phishing attempts using rule-based detection.

## Features

- Detects suspicious keywords and phrases
- Identifies urgency tactics and security bypass attempts
- Recognizes brand impersonation (PayPal, Netflix, Amazon, etc.)
- Detects QR code phishing attempts
- Identifies callback phishing (vishing) phone numbers
- Analyzes URLs for deceptive patterns
- Calculates risk score and provides actionable recommendations



## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation

```bash
git clone https://github.com/Mohamed-Omar-Sayed/DecodeLabs-Phishing-Awareness-Analysis.git
cd DecodeLabs-Phishing-Awareness-Analysis

cd Phishing Awareness Analysis Project
python main.py
```
How to Use
Launch the application

Paste the email content when prompted

Press Enter twice to submit

Review the analysis results

##  Example Output

```text
============================================================
             PHISHING EMAIL DETECTION SYSTEM
============================================================

Paste the email content here (press Enter twice to finish):
--------------------------------------------------

============================================================
ANALYSIS RESULT:
============================================================

Risk Level: HIGH - Confirmed Phishing
Suspicion Score: 85/100
Verdict: This is a dangerous phishing email
Recommended Action: Delete immediately, do not click any links, report to security

Red Flags Detected:
   Suspicious keyword: 'urgent'
   Urgency detected: 'within 24 hours'
   Security bypass: 'confidential'
   Brand impersonation: 'paypal'
   Suspicious link: [http://fake-paypal.com/verify](http://fake-paypal.com/verify)

```
## Detection Rules & Risk Thresholds
1. Threat Scoring Weights

| Category | Score Weight | Description / Threat Indicators |
| :--- | :---: | :--- |
| **Dangerous Attachments** | 30 | Executable or script files (`.exe`, `.bat`) |
| **QR Code Phishing** | 25 | Requests to scan QR codes |
| **Security Bypass** | 20 | Phrases like *Confidential*, *Do not share* |
| **Callback Phishing** | 20 | Fake support numbers for voice impersonation |
| **Urgency Phrases** | 15 | Within 24 hours, Immediately, Act now |
| **Suspicious Links** | 15-20 | URL shorteners or deceptive/typosquatting domains |
| **Brand Impersonation** | 12 | Fake references to known companies (PayPal, Netflix) |
| **Suspicious Keywords** | 10 | Urgent, Verify account, Suspended |






## Customization (phishing_rules.json)
```text
file:JSON{
  "suspicious_keywords": ["urgent", "verify", "suspended"],
  "urgency_phrases": ["within 24 hours", "immediately"],
  "security_bypass_phrases": ["confidential", "do not share"],
  "brand_impersonation": ["paypal", "netflix", "amazon"],
  "qr_code_related": ["scan qr", "qr code"],
  "callback_phishing": ["call us", "customer service"]
}
```
## Testing Scenarios & Samples🚨 

Scenario 1: Phishing Email Sample
```text
From: PayPal <security@paypal-verify.com>
Subject: URGENT: Account Limited

Your account has been suspended due to unusual activity.
Verify your identity immediately: [http://fake-paypal.com](http://fake-paypal.com)
This is confidential. Do not share.
```

Scenario 2: Safe Email Sample
```text
From: john.doe@company.com
Subject: Meeting Agenda

Hi team, please find attached the agenda for tomorrow's meeting.
```
##  Analyst Strategic Review
Current Limitations
```text
1.Does not parse or validate dynamic cryptographic email headers (SPF, DKIM, DMARC).

2.Attachment scanning is limited to static extension identification (does not scan inside buffers).

3.Operational flow requires manual copy-paste of raw email payload text.

4.Rule-based static signature evaluation may yield minor false positives.
```
