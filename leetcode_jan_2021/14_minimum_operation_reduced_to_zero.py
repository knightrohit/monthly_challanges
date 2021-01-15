class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        def min_operation(num_list, val, steps = 0):
            
            if val == 0:
                return steps
            
            if val < 0 or not num_list:
                return float('inf')
            
            if len(num_list) >= 2:
                return min(min_operation(num_list[1:], val - num_list[0], steps + 1),
                           min_operation(num_list[:len(num_list)-1], val - num_list[-1], steps + 1))
            
            elif num_list:
                return min_operation([], val-num_list[-1], steps + 1)
        
        return min_operation(nums, x) if 0 < min_operation(nums, x) < float('inf') else -1