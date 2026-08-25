class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        numset=set(nums)
        for i in range(1,102):
            if i*k in numset:
                continue
            return i*k