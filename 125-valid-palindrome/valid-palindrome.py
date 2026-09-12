class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for char in s:
            if char.isalpha():
                res+=char.lower()
            elif char.isalnum():
                res+=char
        return res==res[::-1]

