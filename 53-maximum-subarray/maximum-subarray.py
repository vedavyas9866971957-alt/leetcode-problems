class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=float("-inf")
        sum=0
        left=0
        for end in range(len(nums)):
            sum+=nums[end]
            maxsum=sum if sum>maxsum else maxsum
            while(sum<0 and left<=end):
                sum=sum-nums[left]
                left+=1
            
            
        return maxsum