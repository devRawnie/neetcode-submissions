class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        next_node = self.root
        for ch in word:
            if ch in next_node.children:
                next_node = next_node.children[ch]
            else:
                node = Node()
                next_node.children[ch] = node
                next_node = node
        next_node.is_end = True

    def search(self, word: str) -> bool:
        next_node = self.root
        for ch in word:
            if ch not in next_node.children:
                return False
            next_node = next_node.children[ch]
        return next_node.is_end

    def startsWith(self, prefix: str) -> bool:
        next_node = self.root
        for ch in prefix:
            if ch not in next_node.children:
                return False
            next_node = next_node.children[ch]
        return True

        