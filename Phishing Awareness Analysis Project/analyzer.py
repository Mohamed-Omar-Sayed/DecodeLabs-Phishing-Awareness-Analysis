from keyword_checker import KeywordChecker
from link_checker import LinkChecker

class PhishingAnalyzer:
    def __init__(self):
        self.keyword_checker = KeywordChecker()
        self.link_checker = LinkChecker()
    
    def analyze(self, email_text):
        all_red_flags = []
        total_score = 0
        
        # Check keywords (returns red_flags, score)
        kw_flags, kw_score = self.keyword_checker.check(email_text)
        all_red_flags.extend(kw_flags)
        total_score += kw_score
        
        # Check links (returns red_flags, score, urls)
        link_result = self.link_checker.check(email_text)
        all_red_flags.extend(link_result['red_flags'])
        total_score += link_result['score']
        
        # Determine result
        if total_score >= 50:
            return {
                'is_phishing': True,
                'risk_level': ' HIGH - Confirmed Phishing',
                'score': min(total_score, 100),
                'red_flags': all_red_flags,
                'verdict': ' This is a dangerous phishing email',
                'action': 'Delete the email immediately, do not click any links, report to security team'
            }
        elif total_score >= 20:
            return {
                'is_phishing': False,
                'risk_level': ' MEDIUM - Suspicious',
                'score': total_score,
                'red_flags': all_red_flags,
                'verdict': ' This email is suspicious',
                'action': 'Verify the sender through another channel before taking any action'
            }
        else:
            return {
                'is_phishing': False,
                'risk_level': ' LOW - Likely Safe',
                'score': total_score,
                'red_flags': all_red_flags,
                'verdict': ' This email appears safe',
                'action': 'You can handle this email normally'
            }