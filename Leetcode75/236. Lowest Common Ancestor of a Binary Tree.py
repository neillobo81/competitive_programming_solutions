# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        elif root == p or root == q:
            return root

        left_ans = self.lowestCommonAncestor(root.left, p, q)
        right_ans = self.lowestCommonAncestor(root.right, p, q)

        if left_ans == None and right_ans == None:
            return None
        elif left_ans == None and right_ans != None:
            return right_ans
        elif left_ans != None and right_ans == None:
            return left_ans
        else:
            return root

        