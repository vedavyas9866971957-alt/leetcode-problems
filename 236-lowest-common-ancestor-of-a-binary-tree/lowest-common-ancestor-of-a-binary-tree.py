# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def containes(root,p,q):
            if root is None:
                return None
            
            if root is p or root is q:
                return root
           

            left=containes(root.left,p,q)
            right=containes(root.right,p,q)
            
            if left and right:
                return root
            if left:
                return left
            return right
        return containes(root,p,q)
            