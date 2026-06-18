# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(tree):
            if tree:
                swap(tree.left)
                temp = tree.left 
                tree.left = tree.right
                tree.right = temp
                swap(tree.left)
        swap(root)
        return root

        