class Node:
    def __init__(self):
        self.children = {}
        self.word = False
        self.complete = None

class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()

            node = node.children[ch]
        node.word = True
        node.complete = word
        
def print_trie(node, prefix="", is_last=True, path=""):
    """
    Pretty prints the trie structure in a tree format.
    """
    connector = "└── " if is_last else "├── "
    
    if path:  # skip printing root
        end_marker = " (end)" if node.word else ""
        print(prefix + connector + path + end_marker)

    prefix += "    " if is_last else "│   "

    children = list(node.children.items())
    for i, (char, child) in enumerate(children):
        is_last_child = i == len(children) - 1
        print_trie(child, prefix, is_last_child, char)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add_word(word)

        R = len(board)
        C = len(board[0])
        # print_trie(trie.root)
        result = set()

        def dfs(i, j, node):
            if node.word:
                result.add(node.complete)
            
            if i < 0 or i >= R:
                return
            if j < 0 or j >= C:
                return
            
            if board[i][j] == "#":
                return

            if board[i][j] not in node.children:
                return

            current = board[i][j]
            board[i][j] = "#"
            dfs(i, j+1, node.children[current])
            dfs(i, j-1, node.children[current])
            dfs(i+1, j, node.children[current])
            dfs(i-1, j, node.children[current])
            board[i][j] = current

        for i in range(R):
            for j in range(C):
                dfs(i, j, trie.root)

        return list(result)