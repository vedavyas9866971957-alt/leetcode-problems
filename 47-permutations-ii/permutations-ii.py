class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        nums.sort()
        used=[False]*n
        res=[]
        def backtrack(path):
            if len(path)==n:
                res.append(path.copy())
                return
            
            for i in range(n):
                if used[i]:
                    continue

                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i]=True

                backtrack(path)

                path.pop()
                used[i]=False
        backtrack([])
        return res