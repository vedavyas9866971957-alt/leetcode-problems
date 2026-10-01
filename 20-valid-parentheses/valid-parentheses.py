class Solution:
    def isValid(self, s: str) -> bool:
        dic={"(":")","[":']',"{":"}"}
        stack=[]
        for char in s:
        
            if char in dic:
                stack.append(char)
            elif stack and dic[stack.pop()]==char:
                continue
            else:
                return False
        if stack:
            return False
        return True
                
