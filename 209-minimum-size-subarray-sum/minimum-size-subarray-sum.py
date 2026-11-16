class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans=len(nums)+1
        left=0
        tot=0
        for right in range(len(nums)):
            tot+=nums[right]
            while tot>=target:
                ans=min(ans,right-left+1)
                tot-=nums[left]
                left+=1
        print(ans)
        return ans if ans!=len(nums)+1 else 0