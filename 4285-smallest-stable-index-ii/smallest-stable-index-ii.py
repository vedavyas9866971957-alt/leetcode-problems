class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        minarr=[0]*n
        minarr[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            if nums[i]<minarr[i+1]:
                minarr[i]=nums[i]
            else:
                minarr[i]=minarr[i+1]

        maximum=nums[0]
        for i in range(n):
            maximum=max(maximum,nums[i])
            if maximum-minarr[i]<=k:
                return i
        return -1
