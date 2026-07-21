# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
        if not p and not q:
            return True
        
        if (not p and q) or (p and not q) or p.val != q.val:
            return False
        else:
            leftChildP = p.left
            rightChildP = p.right

            leftChildQ = q.left
            rightChildQ = q.right

            return self.isSameTree(leftChildP, leftChildQ) and self.isSameTree(rightChildP, rightChildQ)

        
            
        