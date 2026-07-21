# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        equal = True
        if not p and not q:
            equal = True
        elif(not p and q) or (p and not q) or p.val != q.val:
            equal = False
        else:
            equal = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return equal