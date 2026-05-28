class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
        self.length = float('inf')


class Solution(object):

    def update(self, node, word_len, idx):

        if word_len < node.length:
            node.length = word_len
            node.idx = idx

        elif word_len == node.length and idx < node.idx:
            node.idx = idx

    def stringIndices(self, wordsContainer, wordsQuery):
        
        root = TrieNode()

        # Build Trie
        for i, word in enumerate(wordsContainer):

            node = root

            self.update(node, len(word), i)

            for ch in reversed(word):

                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                self.update(node, len(word), i)

        ans = []

        # Search Queries
        for word in wordsQuery:

            node = root
            best = root.idx

            for ch in reversed(word):

                if ch not in node.children:
                    break

                node = node.children[ch]
                best = node.idx

            ans.append(best)

        return ans