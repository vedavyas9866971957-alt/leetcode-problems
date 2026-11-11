class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        freq = {}
        left = 0
        total = 0
        ans = 0

        for right in range(len(nums)):
            total += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            if right - left + 1 > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                total -= nums[left]
                left += 1

            if right - left + 1 == k and len(freq) == k:
                ans = max(ans, total)

        return ans