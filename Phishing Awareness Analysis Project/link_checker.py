import re

class LinkChecker:
    def __init__(self):
        self.url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
        self.shortener_domains = ['bit.ly', 'tinyurl', 'shorturl', 'is.gd', 'ow.ly', 'goo.gl']
        self.suspicious_patterns = ['secure-update', 'verify-account', 'login-security', 'confirm-identity', 'account-verify']
    
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
                    red_flags.append(f" URL shortener detected: {short}")
                    score += 15
            
            for sus in self.suspicious_patterns:
                if sus in url.lower():
                    red_flags.append(f" Suspicious link: {url}")
                    score += 20
            
            if re.search(r'[0-9]{5,}', url):
                red_flags.append(f" Link with many numbers: {url[:50]}...")
                score += 10
        
        return {'red_flags': red_flags, 'score': score, 'urls_found': urls_found}