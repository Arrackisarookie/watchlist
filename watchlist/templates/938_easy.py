#
# 938. Range Sum of BST
#
# Given the root node of a binary search tree, return the sum of values of all
# nodes with value between L and R (inclusive).
#
# The binary search tree is guaranteed to have unique values.
#
# Example 1:
# Input: root = [10, 5, 15, 3, 7, null, 18], L = 7, R = 15
# Output: 32
#
# Example 2:
# Input: root = [10, 5, 15, 3, 7, 13, 18, 1, null, 6], L = 6, R = 10
# Output: 23
#


class Solution:
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if R > node.val:
                    dfs(node.right)
        self.ans = 0
        return self.ans

    def rangeSumBST2(self, root, L, R):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node is not None:
                if L <= node.val <= R:
                    ans += node.val
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans
