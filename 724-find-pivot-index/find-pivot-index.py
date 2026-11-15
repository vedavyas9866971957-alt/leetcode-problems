class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total=sum(nums)
        presum=0
        for i,val in enumerate(nums):
            total-=val
            if total==presum:
                return i
            
            presum+=val
        return -1