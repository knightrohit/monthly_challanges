from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        word_dict = set(wordDict)
        
        @lru_cache(None)
        def wordBreakRecur(s):
            if not s:
                return True
            
            for end in range(1, len(s) + 1):
                if s[0:end] in word_dict and wordBreakRecur(s[end:]):
                    return True                
            return False
        
        return wordBreakRecur(s)