class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ma=nums[0]
        for i in range(len(nums)):
            ma=nums[i] if nums[i]>ma else ma
            mi=nums[i]
            for j in range(i,len(nums)):
                mi=nums[j] if nums[j]<mi else mi
            if ma-mi<=k:
                return i

        return -1
            