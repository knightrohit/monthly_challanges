class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        def backtracking(n, vowel):
            if not n:
                return 1
            
            result = 0
            
            for i in range(vowel, 6):
                result += backtracking(n-1, i)
                
            return result
        
        return backtracking(n, 1)