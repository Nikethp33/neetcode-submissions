class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        p=""
        
        for i in s:
            if i.isalnum():
                p += i.lower()
            else:
                continue

        for i in range(len(p)):
            if p[i] != p[len(p)-1-i]:
                return False

        return True

