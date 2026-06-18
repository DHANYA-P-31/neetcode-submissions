# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def check(root,p,q):
            if root:
                if (p.val < root.val and q.val < root.val):
                    return check(root.left,p,q)
                elif (p.val > root.val and q.val > root.val):
                    return check(root.right,p,q)
                else:
                    return root
        
        return check(root,p,q)