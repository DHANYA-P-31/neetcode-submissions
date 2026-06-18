# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def level(root,l,order):
            if root:
                if order == len(l):
                    l.append([])
                l[order].append(root.val)
                level(root.left,l,order+1)
                level(root.right,l,order+1)
        ans = []
        level(root,ans,0)
        return ans
        