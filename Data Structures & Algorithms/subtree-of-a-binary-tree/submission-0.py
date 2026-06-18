# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(t,s):
            if t and s:
                return t.val == s.val and sameTree(t.left,s.left) and sameTree(t.right,s.right)
            if t or s:
                return False
            return True
        
        def check(t,s):
            if not t:
                return False
            if sameTree(t,s):
                return True
            return check(t.left,s) or check(t.right,s)
        
        return check(root,subRoot)