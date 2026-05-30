import json
import os

class KeywordChecker:
    def __init__(self, rules_file='phishing_rules.json'):
        self.rules = self.load_rules(rules_file)
    
    def load_rules(self, rules_file):
       rules_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'phishing_rules.json')
       with open(rules_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    def check(self, email_text):
        red_flags = []
        score = 0
        
        if not email_text:
            return red_flags, score
        
        email_lower = email_text.lower()
        
        # Check suspicious keywords
        for keyword in self.rules.get('suspicious_keywords', []):
            if keyword in email_lower:
                red_flags.append(f"Suspicious keyword: '{keyword}'")
                score += 10
        
        # Check urgency phrases
        for phrase in self.rules.get('urgency_phrases', []):
            if phrase in email_lower:
                red_flags.append(f"Urgency detected: '{phrase}'")
                score += 15
        
        # Check security bypass phrases
        for phrase in self.rules.get('security_bypass_phrases', []):
            if phrase in email_lower:
                red_flags.append(f"Security bypass: '{phrase}'")
                score += 20
        
        # Check brand impersonation
        for brand in self.rules.get('brand_impersonation', []):
            if brand in email_lower:
                red_flags.append(f"Brand impersonation: '{brand}'")
                score += 12
        
        # Check QR code related phrases
        for phrase in self.rules.get('qr_code_related', []):
            if phrase in email_lower:
                red_flags.append(f"QR code phishing detected: '{phrase}'")
                score += 25
        
        # Check callback phishing phrases
        for phrase in self.rules.get('callback_phishing', []):
            if phrase in email_lower:
                red_flags.append(f"Callback phishing detected: '{phrase}'")
                score += 20
        
        return red_flags, score
