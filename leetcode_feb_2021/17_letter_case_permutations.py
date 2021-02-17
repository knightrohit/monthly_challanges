from itertools import product

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        
        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else (x)
        return list(map(''.join, product(*map(f, S))))