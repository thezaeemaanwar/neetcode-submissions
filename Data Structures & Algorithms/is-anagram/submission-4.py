class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = set(s)

        if len(s) != len(t):
            return False

        for s_char in s:
            if t.count(s_char) != s.count(s_char):
                return False
        return True
            