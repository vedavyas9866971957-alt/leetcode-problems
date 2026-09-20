class Solution:
    def reverseDegree(self, s: str) -> int:
        ans=0
        for pos,char in enumerate(s,1):
            val=123-ord(char)
            ans+=pos*val
        return ans
        