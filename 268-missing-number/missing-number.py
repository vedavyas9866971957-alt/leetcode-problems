class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # sum of 0..n
        return expected_sum - sum(nums)