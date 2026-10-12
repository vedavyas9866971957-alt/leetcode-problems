class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        modulo=10**9+7
        count_bits=[0]*31
        for num in nums:
            for i in range(31):
                if (num>>i)&1:
                    count_bits[i]+=1
        
        ans=0
        for _ in range(k):
            curnum=0
            for i in range(len(count_bits)):
                if count_bits[i]>0:
                    curnum+=2**i
                    count_bits[i]-=1
            ans+=curnum*curnum % modulo
        return ans%modulo