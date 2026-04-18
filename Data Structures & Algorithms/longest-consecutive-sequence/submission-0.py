class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        starters = []
        max_length = 0
        for i in nums_set:
            if i-1 not in nums_set:
                starters.append(i)
        
        for i in range(len(starters)):
            x = starters[i]
            x_list = []
            while x in nums_set:
                x_list.append(x)
                x += 1
            if len(x_list) > max_length:
                max_length = len(x_list)
        
        return max_length
        