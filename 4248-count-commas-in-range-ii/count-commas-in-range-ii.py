class Solution:
    def countCommas(self, n: int) -> int:
        
        lis=[(1000,1),(10**6,2),(10**9,3),(10**12,4),(10**15,5)]
        tcommas=0
        for i in range(0,len(lis)-1):
            if n>=lis[i][0]:
                tcommas+=(min(lis[i+1][0],n+1)-lis[i][0])*lis[i][1]
            else:
                return tcommas
        return  tcommas if n!=10**15 else tcommas+5
        



                