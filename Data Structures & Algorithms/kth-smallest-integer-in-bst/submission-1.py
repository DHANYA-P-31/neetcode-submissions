# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        def inorderTraversal(root):
            if root:
                l = inorderTraversal(root.left)
                if l is not None:
                    return l
                self.count += 1
                if self.count == k:
                    return root.val
                return inorderTraversal(root.right)
            return None
        return inorderTraversal(root)