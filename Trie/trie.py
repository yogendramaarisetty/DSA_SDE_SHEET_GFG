class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.endOfWord = False
        
        def __repr__(self):
            return str(f'{self.children} | {self.endOfWord}')
    
    def __init__(self):
        self.root = self.TrieNode()
    
    def print_trie(self):
        q = [self.root]
        s = set([self.root])
        while len(q) is not 0:
            curr = q.pop(0)
            print(curr.children)
            for c in curr.children:
                q.append(curr.children[c])
    

        

    def insert(self,word):
        curr = self.root
        for i,c in enumerate(word):
            if c not in curr.children:
                curr.children[c] = self.TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self,word):
        curr = self.root
        for i,c in enumerate(word):
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.endOfWord
    
    

if __name__ == "__main__":
    trie = Trie()
    trie.insert("abc")
    print(trie.root)
    print()
    trie.insert("abgl")
    print(trie.root)
    print()
    trie.insert("cdf")
    print(trie.root)
    print()
    trie.insert("abcd")
    trie.print_trie()
    print()
    trie.insert("lmn")
    print(trie.root)
            

    
