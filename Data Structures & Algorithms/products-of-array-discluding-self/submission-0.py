class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.append(1)
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)
        prefix[0] = suffix[n] = 1
        res = [0] * n

        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        
        for i in range(n-1, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]

        for i in range(0,n):
            res[i] = prefix[i] * suffix[i]
        
        return res