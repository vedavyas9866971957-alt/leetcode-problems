class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        t3=0
        t2,t1=1,1
        for _ in range(n-2):
            out=t1+t2+t3
            t3=t2
            t2=t1
            t1=out
        return out
