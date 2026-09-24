# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        queue=deque([root])
        max_level=-1
        max_sum=float("-inf")
        level_num=0
        while queue:
            level_num+=1
            length=len(queue)
            sum_level=0
            for _ in range(length):
                
                curr=queue.popleft()
                sum_level+=curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            if sum_level>max_sum:
                max_level=level_num
                max_sum=sum_level
        return max_level
