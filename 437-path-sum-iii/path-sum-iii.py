class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:

        def dfs(root, prefix, total):
            if root is None:
                return 0

            total += root.val

            count = prefix.get(total - targetSum, 0)

            prefix[total] = prefix.get(total, 0) + 1

            count += dfs(root.left, prefix, total)
            count += dfs(root.right, prefix, total)

            prefix[total] -= 1

            return count

        return dfs(root, {0: 1}, 0)