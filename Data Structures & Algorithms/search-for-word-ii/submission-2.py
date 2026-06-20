class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.idx = -1
        self.ref = 0
    
    def addWord(self,word,i):
        cur = self
        cur.ref += 1
        for w in word:
            index = ord(w) - ord('a')
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
            cur.ref += 1
        cur.idx = i


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i],i)
        n = len(board)
        m = len(board[0])
        ans = []

        def getIndex(c):
            return ord(c) - ord('a')
        def search(r,c,node):
            if r < 0 or c < 0 or r >= n or c >= m or board[r][c] == "*" or not node.children[getIndex(board[r][c])]:
                return
            tmp = board[r][c]
            board[r][c] = '*'
            prev = node
            node = node.children[getIndex(tmp)]
            if node.idx != -1:
                ans.append(words[node.idx])
                node.idx = -1
                node.ref -= 1
                if not node.ref:
                    prev.children[getIndex(tmp)] = None
                    node = None
                    board[r][c] = tmp
                    return
            search(r+1,c,node)
            search(r-1,c,node)
            search(r, c+1,node)
            search(r, c-1, node)
            board[r][c] = tmp
            
        for i in range(n):
            for j in range(m):
                search(i,j,root)
        return ans
