import re

class LinkChecker:
    def __init__(self):
        self.url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
        self.shortener_domains = [
            'bit.ly', 'tinyurl', 'shorturl', 'is.gd', 'ow.ly', 'goo.gl',
            'zya.me', 'cutt.ly', 'rebrand.ly', 'short.link', 'tiny.cc',
            'shorte.st', 'clicky', 'adf.ly', 'bc.vc', 't.co'
        ]
        self.suspicious_patterns = [
            'secure-update', 'verify-account', 'login-security', 'confirm-identity', 
            'account-verify', 'microsoft', 'outlook', 'office365', 'mail-soft',
            'account-security', 'verify-identity', 'suspended', 'restore-access'
        ]
    
    def check(self, email_text):
        red_flags = []
        score = 0
        urls_found = []
        
        if not email_text:
            return {'red_flags': red_flags, 'score': score, 'urls_found': urls_found}
        
        urls_found = re.findall(self.url_pattern, email_text)
        
        for url in urls_found:
            for short in self.shortener_domains:
                if short in url.lower():
                    red_flags.append(f"URL shortener detected: {short}")
                    score += 15
            
            for sus in self.suspicious_patterns:
                if sus in url.lower():
                    red_flags.append(f"Suspicious link pattern: {sus} in {url[:60]}...")
                    score += 20
            
            
            if re.search(r'[0-9a-f]{10,}', url):
                red_flags.append(f"Random characters in URL: {url[:50]}...")
                score += 10
            
            
            if '@' in url:
                red_flags.append(f"Suspicious URL with @ symbol: {url[:50]}...")
                score += 25
            
           
            suspicious_domains = ['.zya.', '.tk', '.ml', '.ga', '.cf', '.xyz', '.top', '.click']
            for sus_domain in suspicious_domains:
                if sus_domain in url.lower():
                    red_flags.append(f"Suspicious TLD detected: {sus_domain}")
                    score += 15
        
        return {'red_flags': red_flags, 'score': score, 'urls_found': urls_found}
