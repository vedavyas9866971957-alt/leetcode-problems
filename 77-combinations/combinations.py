class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res=[]
        def backtrack(comb,f):
            if len(comb)>k:
                return 
            if len(comb)==k:
                res.append(comb.copy())
                return
            for i in range(f,n+1):
                #choose
                comb.append(i)
                #backtrack
                backtrack(comb,i+1)
                #unchoose
                comb.pop()
        backtrack([],1)
        return res
            