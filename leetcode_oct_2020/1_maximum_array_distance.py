"""
Time Complexity = O(N^2)
Space Complexity = O(1)
"""
# TLE
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        out = 0
        for i in range(len(arrays)):
            imin = arrays[i][0]
            imax = arrays[i][-1] if len(arrays) >= 2 else None
            for j in range(i+1, len(arrays)):
                nmin = arrays[j][0]
                nmax = arrays[j][-1] if len(arrays) >=2 else None
                if nmax:
                    out = max(out, abs(imin - nmax))
                if imax:
                    out = max(out, abs(nmin - imax))
                if not nmax and not imax:
                    out = max(out, abs(nmin - imin))
        return out


"""
Time Complexity = O(N)
Space Complexity =  O(Size of array)
"""
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        imax, max_indx = max((array[-1], indx) for indx, array in enumerate(arrays))
        imin, min_indx = min((array[0], indx) for indx, array in enumerate(arrays))
        
        fmax = max(imax - array[0] for indx, array in enumerate(arrays) if indx != max_indx)
        fminmax = max(array[-1] -  imin for indx, array in enumerate(arrays) if indx != min_indx)
        
        return max(fmax, fminmax)