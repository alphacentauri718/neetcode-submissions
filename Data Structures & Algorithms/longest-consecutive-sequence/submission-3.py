class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for i in nums_set:
            if i-1 not in nums_set:
                x = i
                length = 1
                while x + length in nums_set:
                    length += 1
                if length > max_length:
                    max_length = length
        
        return max_length
        