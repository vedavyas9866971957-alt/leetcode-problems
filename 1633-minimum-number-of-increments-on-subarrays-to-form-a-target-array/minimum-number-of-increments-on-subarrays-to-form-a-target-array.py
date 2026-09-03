class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res=0
        prev=0
        for i in range(len(target)):
            if target[i]>prev:
                res+=target[i]-prev
            prev=target[i]
        return res