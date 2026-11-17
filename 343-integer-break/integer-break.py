class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:
            return n-1
        threes=n//3
        rem=n%3
        if rem==1:
            threes-=1
            rem+=3
        if rem==0:
            rem=1
        return pow(3,threes)*rem