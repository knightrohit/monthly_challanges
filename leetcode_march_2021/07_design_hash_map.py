"""
Time/Space Complexity = O(N)
"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lkp = set()
        self.val = [0]*(10**6+1)
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.lkp.add(key)
        self.val[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key not in self.lkp:
            return -1
        else:
            return self.val[key]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.lkp:
            self.lkp.remove(key)
            self.val[key] = 0