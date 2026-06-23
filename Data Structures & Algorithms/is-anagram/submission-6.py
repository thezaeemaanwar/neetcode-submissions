class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()

        for s_char in s:
            if s_char in s_dict:
                s_dict[s_char] += 1
            else:
                s_dict[s_char] = 1

        for t_char in t:
            if t_char in t_dict:
                t_dict[t_char] += 1
            else:
                t_dict[t_char] = 1
        
        return s_dict == t_dict
            