class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:

        n = len(nums)

        # Calculate the total sum of the array
        total = sum(nums)

        # Sum of the subarray that we want to keep
        target = total - x

        # Special case:
        # If target is negative, no remaining subarray
        # can have a negative sum because all numbers are positive.
        if target < 0:
            return -1

        # If target is zero, we must remove every element.
        if target == 0:
            return n

        left = 0
        current_sum = 0
        max_length = -1

        # Sliding window
        for right in range(n):

            # Expand the window
            current_sum += nums[right]

            # Shrink the window if sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1

            # If the current window has the target sum
            if current_sum == target:
                length = right - left + 1

                # Store the longest valid subarray
                max_length = max(max_length, length)

        # If no valid subarray was found
        if max_length == -1:
            return -1

        # Minimum removals = total elements - kept elements
        return n - max_length