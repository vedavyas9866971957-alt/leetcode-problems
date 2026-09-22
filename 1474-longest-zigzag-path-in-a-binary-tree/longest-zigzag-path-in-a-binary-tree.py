
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root):
        self.answer = 0

        def dfs(node, direction, length):
            # If the node is None, stop recursion.
            if node is None:
                return

            # Update the global maximum.
            self.answer = max(self.answer, length)

            # If the previous move was LEFT,
            # the next move should be RIGHT.
            if direction == "left":

                # Continue the ZigZag:
                # Move right and increase length.
                dfs(node.right, "right", length + 1)

                # Start a new ZigZag from the left child.
                # Length becomes 1 because we made one edge.
                dfs(node.left, "left", 1)

            else:

                # Continue the ZigZag:
                # Move left and increase length.
                dfs(node.left, "left", length + 1)

                # Start a new ZigZag from the right child.
                # Length becomes 1 because we made one edge.
                dfs(node.right, "right", 1)

        # Start from the root in both directions.
        dfs(root.left, "left", 1)
        dfs(root.right, "right", 1)

        return self.answer