# 872. Leaf-Similar Trees
#Easy
#problem statement: https://leetcode.com/problems/leaf-similar-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafValue1 = self.getLeafvalue(root1)
        leafValue2 = self.getLeafvalue(root2)

        return (leafValue1 == leafValue2)

    def getLeafvalue(self, root: Optional[TreeNode]) -> bool:
        if root is None: 
            return [] 
        elif root.left is None and root.right is None:
            return [root.val]
        res = []
        res.extend(self.getLeafvalue(root.left))
        res.extend(self.getLeafvalue(root.right))
        return res

        