from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque(maxlen = self.size)
        self.avg = 0
        

    def next(self, val: int) -> float:

        if len(self.queue) >= self.size:
            self.queue.popleft()
        
        self.queue.append(val)
        self.avg = sum(self.queue)/len(self.queue)
        return self.avg