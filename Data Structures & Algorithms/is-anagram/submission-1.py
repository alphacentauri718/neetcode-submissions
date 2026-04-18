class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = list(s)
        t_arr = list(t)
        counts_s = {}
        counts_t = {}

        if len(s) != len(t):
            return False

        for i in s_arr:
            counts_s[i] = counts_s.get(i, 0) + 1
        for j in t_arr:
            counts_t[j] = counts_t.get(j, 0) + 1
        
        return counts_t == counts_s
        