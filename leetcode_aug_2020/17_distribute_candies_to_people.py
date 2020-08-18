"""
Time/Space Complexity = O(N)
"""
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        out = [0]*num_people
        loop = 0
        while candies > 0:
            for indx, val in enumerate(out):
                temp = candies - (num_people*loop + indx + 1)
                if temp > 0:
                    out[indx] += num_people*loop + indx + 1
                    candies -= num_people*loop + indx + 1

                else:
                    out[indx] += candies
                    candies -= candies
                    break
            loop += 1
        return out