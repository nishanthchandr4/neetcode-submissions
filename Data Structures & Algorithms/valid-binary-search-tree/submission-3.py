# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.valid = True

        def dfs(root, boundary):
            if not root:
                return
            
            if not (root.val > boundary[0] and root.val < boundary[1]):
                self.valid = False

            dfs(root.left, [boundary[0], root.val])
            dfs(root.right, [root.val, boundary[1]])
            
        dfs(root, [-10000, 10000])
        return self.valid
        
