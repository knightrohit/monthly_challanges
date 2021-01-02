"""
Time/Space Complexity = O(N)
"""
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        d = dict()
        
        for i in pieces:
            if len(i) == 1:
                d[i[0]] = None
            else:
                d[i[0]] = i[1:]
        
        list_val = []
        found = True
        indx = 0

        for i in arr:
            if list_val and indx < len(list_val):
                if list_val[indx] == i:
                    indx += 1
                    continue
                else:
                    found = False
                    break                
            else:
                indx = 0
                if i in d:
                    list_val = d[i]
                    continue
                else:
                    found = False
                    
        return found