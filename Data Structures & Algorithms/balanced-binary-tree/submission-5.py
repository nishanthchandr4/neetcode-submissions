# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(root):
            if not root:
                return 0
            else:

                height = 1
                leftHeight = dfs(root.left)
                rightHeight = dfs(root.right)

                if abs(rightHeight - leftHeight) > 1:
                    self.balanced = False


                if leftHeight > rightHeight:
                    height += leftHeight
                else:
                    height += rightHeight

                return height
            
        dfs(root)
        return self.balanced



        