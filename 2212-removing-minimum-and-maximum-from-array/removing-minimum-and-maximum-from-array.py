class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return n
        minind=0
        maxind=0
        for i,val in enumerate(nums):
            if val<nums[minind]:
                minind=i
            if val>nums[maxind]:
                maxind=i
        
        left=min(maxind,minind)
        right=max(maxind,minind)
        leftfirst=left+1+min(right-left,n-right)
        rightfirst=n-right+min(left+1,right-left)
        return min(leftfirst,rightfirst)