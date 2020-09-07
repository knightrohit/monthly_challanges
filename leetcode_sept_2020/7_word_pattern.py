"""
Time/Space Complexity = O(N)
"""
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
        if not (pattern and str) or len(pattern) != len(str.split()):
            return False
        
        word_dict = dict()
        str_list = str.split()
        added = set()

        for i in range(len(str_list)):
            
            val = word_dict.get(pattern[i])
            if not val and str_list[i] not in added:
                word_dict[pattern[i]] = str_list[i]
                added.add(str_list[i])
                continue
            
            if val != str_list[i]:
                return False

        return True