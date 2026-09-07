class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp=[0]*(len(s)+1)
        dp[0]=1
        dic={}
        for i,c in enumerate(s,1):
            if c in dic:
                dp[i]=2*dp[i-1]-dp[dic[c]-1]
                
            else:
                dp[i]=2*dp[i-1]
            print(i,dp[i])
            dic[c]=i
        return(dp[len(s)]-1) % (10**9 + 7)