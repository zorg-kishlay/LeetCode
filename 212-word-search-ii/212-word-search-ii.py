class TrieNode:
    def __init__(self):
        self.children={}
        self.isEnd = False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word):
        curr = self.root
        
        for ch in word:
            curr = curr.children.setdefault(ch,TrieNode())
        
        curr.isEnd=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows,cols = len(board),len(board[0])
        self.total_words = len(words)
        result = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        visited = set()
        
        def dfs(node,i,j,path):
            
            if self.total_words ==0:
                return
            if node.isEnd:
                result.append(path)
                node.isEnd = False # to avoid words which contain the same starting characters
                self.total_words-=1
            
            if i<0 or j<0 or i >= rows or j>=cols or board[i][j] not in node.children or (i,j) in visited:
                return
            
            # reaching here means that the word is present in Trie
            visited.add((i,j))
            tmp = board[i][j]
            for x,y in [(0,1),(0,-1),(-1,0),(1,0)]:
                # check in the children of the current Trie node
                dfs(node.children[tmp],i+x,j+y,path+tmp)
            visited.remove((i,j))
        
        # check for each element in the board
        for i in range(rows):
            for j in range(cols):
                dfs(trie.root,i,j,"")
        
        return result