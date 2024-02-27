# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.ans = 0
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            # Update the diameter (ans)
            self.ans = max(self.ans, left + right)

            # Return the height of the tree rooted at this node
            return max(left, right) + 1

        height(root)
        return self.ans