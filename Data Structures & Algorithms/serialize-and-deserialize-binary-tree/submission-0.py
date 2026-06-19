# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        self.s= ""
        def preorder(root):
            if root:
                self.s += str(root.val)+","
                preorder(root.left)
                preorder(root.right)
            else:
                self.s += "N,"
        preorder(root)
        return self.s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l = data.split(",")
        self.i = 0
        def dfs():
            if l[self.i] == "N" or l[self.i] == "":
                self.i += 1
                return None
            t = TreeNode(int(l[self.i]))
            self.i += 1
            t.left = dfs()
            t.right = dfs()
            return t
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))