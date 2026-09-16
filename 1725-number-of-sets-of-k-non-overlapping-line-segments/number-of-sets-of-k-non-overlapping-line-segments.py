from functools import cache

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(i, remaining, drawing):
            # We have no more segments to create.
            if remaining == 0:
                return 1

            # No points left, but segments are still required.
            if i == n:
                return 0

            if drawing:
                # Option 1: Extend the current segment to the next point.
                extend = dp(i + 1, remaining, True)

                # Option 2: Stop the current segment here.
                stop = dp(i, remaining - 1, False)

                return (extend + stop) % MOD

            else:
                # Option 1: Skip this point.
                skip = dp(i + 1, remaining, False)

                # Option 2: Start a segment at this point.
                start = dp(i + 1, remaining, True)

                return (skip + start) % MOD

        return dp(0, k, False)