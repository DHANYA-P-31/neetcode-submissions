# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root,min_r,max_r):
            if root:
                if root.val >= max_r or root.val <= min_r:
                    return False
                return valid(root.left,min_r,root.val) and valid(root.right,root.val,max_r)
            return True

        return valid(root,-math.inf,math.inf)

