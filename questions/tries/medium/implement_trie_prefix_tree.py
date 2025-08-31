class Node:
    def __init__(self, end=False):
        self.end = end
        self.children = {}

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for let in word:
            if let not in current.children.keys():
                current.children[let] = Node()
                current = current.children[let]
            else:
                current = current.children[let]

        current.end = True

    def search(self, word: str) -> bool:
        current = self.root
        for let in word:
            if let not in current.children.keys():
                return False
            else:
                current = current.children[let]

        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for let in prefix:
            if let not in current.children.keys():
                return False
            else:
                current = current.children[let]

        return True
