class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        nums=[-i if i<0 else i  for i in nums]
        nums.sort(reverse=True)
        score=0
        if n%2==0:
            for num in nums[:n//2]:
                score+=num*num
            for num in nums[n//2:]:
                score-=num*num
        else:
            for num in nums[:n//2+1]:
                score+=num*num
            for num in nums[n//2+1:]:
                score-=num*num
        return score