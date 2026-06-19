class TrieNode:
    def __init__(self):
        # A dictionary mapping characters to their respective TrieNode objects
        self.children = {}
        # Flag indicating if the path from the root to this node constitutes a whole word
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie. Time Complexity: O(L)"""
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """Returns True if the exact word is in the trie. Time Complexity: O(L)"""
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """Returns True if there is any word in the trie that starts with the given prefix. Time Complexity: O(L)"""
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

# --- Verification & Testing ---
trie = Trie()
trie.insert("apple")
print("Search 'apple':", trie.search("apple"))   # Returns True
print("Search 'app':", trie.search("app"))       # Returns False (it's only a prefix right now)
print("StartsWith 'app':", trie.startsWith("app")) # Returns True
trie.insert("app")
print("Search 'app' after inserting:", trie.search("app")) # Returns True