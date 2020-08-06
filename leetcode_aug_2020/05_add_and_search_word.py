"""
Time Complexity = O(M*N) , M = no of keys, N - no of dots
Space Compleixty = O(M)
"""
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        x = self.trie
        for ch in word:
            x = x.setdefault(ch, {})
        x['$'] = True
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(word, trie):        
            
            for indx, ch in enumerate(word):
                if not ch in trie:
                    if ch == '.':
                        for key in trie:
                            if key != '$' and dfs(word[indx + 1:], trie[key]):
                                return True                        
                    return False
                
                else:
                    trie = trie.get(ch)

            return '$' in trie
        
        return dfs(word, self.trie)