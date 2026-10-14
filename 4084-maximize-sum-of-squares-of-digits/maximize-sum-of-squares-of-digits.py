class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res=[]
        cursum=0
        for _ in range(num):
            for digit in range(9,-1,-1):
                if cursum+digit<=sum:
                    res.append(str(digit))
                    cursum+=digit
                    break
        return "".join(res) if cursum==sum else ""