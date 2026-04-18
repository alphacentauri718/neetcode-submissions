import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ret = []

        #if length > 0, pick word
        while len(strs) > 0:
            my_dict = {char: 0 for char in string.ascii_lowercase}
            word = list(strs[0])
            for letter in word:
                my_dict[letter] += 1

            #iterate through list adding anagrams to items
            items = [strs[0]]
            for i in range(1, len(strs)):
                i_word = list(strs[i])
                my_dict2 = {char: 0 for char in string.ascii_lowercase}
                for letter in i_word:
                    my_dict2[letter] += 1
                if my_dict == my_dict2:
                    items.append(strs[i])
            ret.append(items)
            for j in items:
                strs.remove(j)
        return ret
        