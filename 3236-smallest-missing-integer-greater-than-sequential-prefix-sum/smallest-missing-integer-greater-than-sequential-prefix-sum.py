class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        se=set(nums)
        su=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                su+=nums[i]
            else:
                break
      
        for out in range(su,su+len(nums)+1):
            if out not in se:
                return out