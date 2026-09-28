class Solution:
    def maxDepth(self, s: str) -> int:
        stacklen=0
        maximum_depth=0
        for char in s:
            if char=='(':
                stacklen+=1
            if char==")":
                maximum_depth=max(maximum_depth,stacklen)
                stacklen-=1
        return maximum_depth