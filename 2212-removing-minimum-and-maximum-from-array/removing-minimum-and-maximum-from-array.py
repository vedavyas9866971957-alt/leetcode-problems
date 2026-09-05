class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minind=0
        maxind=0
        for i,val in enumerate(nums):
            if val<nums[minind]:
                minind=i
            if val>nums[maxind]:
                maxind=i
        n=len(nums)
        left=min(maxind,minind)
        right=max(maxind,minind)
        leftfirst=left+1+min(right-left,n-right)
        rightfirst=n-right+min(left+1,right-left)
        return min(leftfirst,rightfirst)