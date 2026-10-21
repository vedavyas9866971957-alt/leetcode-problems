class Solution:
    def minOperations(self, s: str) -> int:
        def issorted(s):
            for i in range(1,len(s)):
                if s[i-1]>s[i]:
                    return False
            return True
        if issorted(s):
            return 0
        if len(s)==2:
            return -1
        mi=min(s)
        ma=max(s)
        if mi==s[0] or ma==s[-1]:
            return 1
        if s.count(mi)>1 or s.count(ma)>1:
            return 2
        if mi==s[-1] and ma==s[0]:
            return 3
        else:
            return 2
        

        