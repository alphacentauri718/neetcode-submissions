class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ret = []
        my_dict = {}
        for i in nums:
            my_dict[i] = my_dict.get(i, 0) + 1
        sorted_dict = list(reversed(sorted(my_dict.items(), key=lambda item: item[1])))[:k]

        for key, value in sorted_dict:
            ret.append(key)
        return ret