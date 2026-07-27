# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if root.val > p.val and root.val > q.val:
            #no need to check if root.left exists because it is garunteed by the problem
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            #no need to check if root.right exists because it is garunteed by the problem
            return self.lowestCommonAncestor(root.right, p, q)
        else: #this case includes the when p or q equals the root
            return root



        



            