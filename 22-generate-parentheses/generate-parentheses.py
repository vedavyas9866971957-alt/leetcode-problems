class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res=[]
        def backtrack(path,opencount,closecount):
            if len(path)==2*n:
                res.append("".join(path))
                return
            if opencount<n:
                path.append("(")
                backtrack(path,opencount+1,closecount)
                path.pop()
            if opencount>closecount:
                path.append(")")
                backtrack(path,opencount,closecount+1)
                path.pop()
        backtrack([],0,0)
        return res