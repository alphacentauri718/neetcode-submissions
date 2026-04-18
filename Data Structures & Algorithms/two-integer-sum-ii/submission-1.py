class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers) - 1
        i = 0
        sum = math.inf
        while sum != target:
            sum = numbers[i] + numbers[n]
            if sum == target:
                return [i + 1, n + 1]
            elif sum > target:
                n -= 1
            else:
                i += 1