class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        a, b = 0, len(s)-1

        while a < b:
            while not s[a].isalnum() and a < b:
                a += 1
            while not s[b].isalnum() and b > a:
                b -= 1
            if s[a].lower() != s[b].lower():
                return False
            a += 1
            b -= 1
        
        return True