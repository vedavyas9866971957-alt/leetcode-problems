class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        def is_perfect_square(n):
            x = int(pow(n, 0.5))
            return x * x == n

        nums.sort()  # Sort to easily skip duplicates
        n = len(nums)
        used = [False] * n
        res = 0

        def backtrack(path):
            nonlocal res  # Fixes the scope error
            
            if len(path) == n:
                res += 1
                return

            for i in range(n):
                if used[i]:
                    continue
                
                # Skip duplicate elements at the same level
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                # Check if the sum with the previous element forms a perfect square
                if path and not is_perfect_square(path[-1] + nums[i]):
                    continue

                path.append(nums[i])
                used[i] = True
                
                backtrack(path)
                
                # Backtrack
                path.pop()
                used[i] = False

        backtrack([])
        return res
