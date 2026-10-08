class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        res=[]
        for i,ch in enumerate(s):
            if ch=="(":
                stack.append(i)
            else:
                if len(stack)==1:
                    res.append(s[stack[0]+1:i])
                stack.pop()
        return "".join(res)
                    
             