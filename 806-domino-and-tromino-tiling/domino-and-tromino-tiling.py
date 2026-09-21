class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        a = 1  # dp[i-3]
        b = 1  # dp[i-2]
        c = 2  # dp[i-1]

        for i in range(3, n + 1):
            d = (2 * c + a) % MOD
            a, b, c = b, c, d

        return c