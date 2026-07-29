class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        curr_power_of_two = 1

        for i in range(1, n + 1):
            if curr_power_of_two * 2 == i:
                curr_power_of_two = i
            
            dp[i] = dp[i - curr_power_of_two] + 1
        
        return dp