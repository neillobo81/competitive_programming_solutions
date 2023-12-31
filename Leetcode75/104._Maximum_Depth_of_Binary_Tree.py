# 104. Maximum Depth of Binary Tree
#Easy
#problem statement: https://leetcode.com/problems/maximum-depth-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
        
