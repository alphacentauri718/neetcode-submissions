class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        differences = {}
        for i in range(n):
            difference = target - nums[i]
            if nums[i] in differences:
                return [list(differences).index(nums[i]), i]
            else:
                differences[difference] = nums[i]
        
        
        