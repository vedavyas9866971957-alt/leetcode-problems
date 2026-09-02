class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        INF=float("inf")
        dp=[INF]*(sum+1)
        dp[0]=0
        for num in nums:
            choices=[]
            n=num
            cost=0
            #multiplication choices
            while(n<=sum):
                choices.append((n,cost))
                n*=2
                cost+=1
            
            #division choices
            n=num//2
            cost=1
            while(n>0):
                if n<=sum:
                    choices.append((n,cost))
                n//=2
                cost+=1
            
            newdp=dp[:]
            for cursum in range(sum+1):
                if dp[cursum]==INF:
                    continue
                for choice in choices:
                    val,cost=choice
                    newsum=cursum+val
                    if newsum<=sum:
                        newdp[newsum]=min(newdp[newsum],dp[cursum]+cost)

            dp=newdp
        return -1 if dp[sum]==INF else dp[sum]