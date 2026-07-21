# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(root):
            if not root:
                return 0 
            else:
                length = 1

                leftChild = root.left
                rightChild = root.right

                leftSide = dfs(leftChild)
                rightSide = dfs(rightChild)

                if leftSide > rightSide:
                    length += leftSide
                else:
                    length += rightSide

                self.diameter = max(self.diameter, leftSide + rightSide)
                return length
        
        length = dfs(root)

        return max(length - 1, self.diameter)

        
                



        