class Node:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        n = self.root
        for ch in word:
            if ch not in n.children:
                n.children[ch] = Node()
            n = n.children[ch]
        n.word = True

    def search(self, word: str) -> bool:
        def dfs(i, n):
            if not n:
                return False

            if i == len(word):
                return n.word

            ch = word[i]
            if ch == ".":
                for child in n.children:
                    if dfs(i+1, n.children[child]):
                        return True

            # print('node', n)
            return dfs(
                i+1,
                n.children.get(word[i])
            )

        return dfs(0, self.root)
