# Trie


class TrieNode:
    def __init__(self):
        self.children = {}  # Map from char to TrieNode
        self.is_end = False  # Marks end of a word
        self.count = 0  # Number of words with this prefix
        self.word_count = 0  # Number of words ending here


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root
        # Track path from root to leaf
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.is_end = True
        node.word_count += 1

    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie."""
        node = self._traverse(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Returns True if there is any word in the trie that starts with the given prefix."""
        return self._traverse(prefix) is not None

    def count_words_with_prefix(self, prefix: str) -> int:
        """Returns the number of words that have the given prefix."""
        node = self._traverse(prefix)
        return node.count if node else 0

    def count_words_equal_to(self, word: str) -> int:
        """Returns the number of occurrences of the exact word."""
        node = self._traverse(word)
        return node.word_count if node and node.is_end else 0

    def delete(self, word: str) -> bool:
        """Delete a word from the trie. Returns True if word was deleted."""
        if not word:
            return False

        # Helper function to recursively delete
        def _delete_helper(node: TrieNode, word: str, depth: int) -> bool:
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                node.word_count -= 1
                return True

            char = word[depth]
            if char not in node.children:
                return False

            deleted = _delete_helper(node.children[char], word, depth + 1)
            if deleted:
                node.children[char].count -= 1
                # Remove node if it's no longer needed
                if node.children[char].count == 0:
                    del node.children[char]
            return deleted

        return _delete_helper(self.root, word, 0)

    def _traverse(self, prefix: str) -> TrieNode:
        """Helper function to traverse to the node representing prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def get_words_with_prefix(self, prefix: str) -> list:
        """Returns all words that start with the given prefix."""
        results = []
        node = self._traverse(prefix)

        if not node:
            return results

        # Helper function for DFS
        def _dfs(node: TrieNode, current_word: str):
            if node.is_end:
                results.append(current_word)

            for char, child in node.children.items():
                _dfs(child, current_word + char)

        _dfs(node, prefix)
        return results

    def get_longest_common_prefix(self) -> str:
        """Returns the longest common prefix among all words in the trie."""
        if not self.root.children:
            return ""

        prefix = []
        node = self.root

        # Keep going while we only have one child and haven't reached the end
        while len(node.children) == 1 and not node.is_end:
            char = next(iter(node.children))
            prefix.append(char)
            node = node.children[char]

        return "".join(prefix)


def demonstrate_trie():
    # Create trie and insert words
    trie = Trie()
    words = ["apple", "app", "apricot", "bear", "bearing", "bee"]

    print("Inserting words:", words)
    for word in words:
        trie.insert(word)

    # Demonstrate basic operations
    print("\nBasic operations:")
    test_words = ["apple", "app", "apt", "bear"]
    for word in test_words:
        print(f"Search '{word}': {trie.search(word)}")
        print(f"Starts with '{word}': {trie.starts_with(word)}")

    # Demonstrate prefix operations
    prefixes = ["ap", "be", "c"]
    print("\nPrefix operations:")
    for prefix in prefixes:
        print(f"\nPrefix '{prefix}':")
        print(f"Count words with prefix: {trie.count_words_with_prefix(prefix)}")
        print(f"Words with prefix: {trie.get_words_with_prefix(prefix)}")

    # Demonstrate deletion
    print("\nDeletion operations:")
    words_to_delete = ["apple", "notfound", "bear"]
    for word in words_to_delete:
        deleted = trie.delete(word)
        print(f"Delete '{word}': {deleted}")
        print(f"Search after deletion: {trie.search(word)}")

    # Demonstrate longest common prefix
    print("\nLongest common prefix:", trie.get_longest_common_prefix())


# Example usage
if __name__ == "__main__":
    demonstrate_trie()
