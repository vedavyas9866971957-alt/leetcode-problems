class Trie:

    def __init__(self):
        self.children={}
    

    def insert(self, word: str) -> None:
        node=self
        for ch in word:
            if ch not in node.children:
                node.children[ch]=Trie()
            node=node.children[ch]
        node.children["#"]=True

    def search(self, word: str) -> bool:
        x=self._walk(word)
        return x is not None and "#" in x.children

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None
    def _walk(self,text):
        node=self
        for ch in text:
            if ch not in node.children:
                return None
            node=node.children[ch]
        return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)