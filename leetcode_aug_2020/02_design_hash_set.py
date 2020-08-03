"""
Time Complexity = O(1)
Space Complexity = O(N)
"""
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = [False]

    def add(self, key: int) -> None:
        if key + 1 > len(self.list):
            self.list += [False]*(key + 1 - len(self.list))
            
        if not self.list[key - 1]:
            self.list[key - 1] = True

    def remove(self, key: int) -> None:
        if key + 1  > len(self.list):
            return False

        self.list[key - 1] = False
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key + 1  > len(self.list):
            return False
        return self.list[key - 1]