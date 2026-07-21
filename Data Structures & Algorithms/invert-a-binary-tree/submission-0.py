
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        else:
            #temporary children holders
            leftChild = root.left
            rightChild = root.right

            #swap the nodes
            root.left = rightChild
            root.right = leftChild

            #go down the tree
            self.invertTree(leftChild)
            self.invertTree(rightChild)

            return root
        
        



        

        