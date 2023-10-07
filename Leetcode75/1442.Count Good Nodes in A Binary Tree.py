# 1442. Count Good Nodes in Binary Tree
#Medium
#problem statement: https://leetcode.com/problems/count-good-nodes-in-binary-tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.findGoodNodes(root, root.val)


    def findGoodNodes(self, root: TreeNode, maxNum: int) -> int:
        additional_node = 0
        if root == None:
            return additional_node
        elif root.val >= maxNum:
            maxNum = root.val
            additional_node = 1

        
        res = self.findGoodNodes(root.left, maxNum) + self.findGoodNodes(root.right, maxNum)
        return res + additional_node