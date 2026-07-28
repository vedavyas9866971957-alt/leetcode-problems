class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        if n%2==1:
            middle_character=s[n//2]
            s=s[:n//2]
            s=sorted(s)
            s="".join(s)
            return s+middle_character+s[::-1]
        else:
            s=s[:n//2]
            s=sorted(s)
            s="".join(s)
            return s+s[::-1]