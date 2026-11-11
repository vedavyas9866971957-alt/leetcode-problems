class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        left=0
        right=0
        ans=0
        while(right<len(nums) and left<len(nums)):
            if nums[left]==0:
                left+=1
            else:
                right=left
                while(right<len(nums)  and nums[right]==1):
                    right+=1
                ans=max(ans,right-left)
                left=right
        return ans
