from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []

        for i in range(len(nums)-1):
            target  = nums[i] * -1
            j = i + 1
            k = len(nums) - 1
            while j < k :
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    res = [nums[i], nums[j], nums[k]]
                    if res not in result:
                        result.append([nums[i], nums[j], nums[k]])
                    j += 1
        return result

