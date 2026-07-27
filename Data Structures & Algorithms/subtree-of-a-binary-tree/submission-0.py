# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(subRoot, root):
            if not subRoot and not root:
                return True
            elif subRoot and not root or not subRoot and root:
                return False
            else:
                if subRoot.val != root.val:
                    return False
                else:
                    leftSide = sameTree(subRoot.left, root.left)
                    rightSide = sameTree(subRoot.right, root.right)
                    return leftSide and rightSide

        if not root:
            return False
        if sameTree(subRoot, root):
            return True     
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        
            






        
        
        
        




        
        