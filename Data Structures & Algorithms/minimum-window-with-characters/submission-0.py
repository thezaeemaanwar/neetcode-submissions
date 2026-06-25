class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        my_hash = dict()
        left, found = 0, 0

        for char in t:
            my_hash[char] = 1 + my_hash.get(char, 0)

        for right in range(len(s)):
            if s[right] in my_hash:
                if my_hash[s[right]] > 0:
                    found += 1

                my_hash[s[right]] -= 1

            while found == len(t):
                if not res or len(res) > (right - left + 1):
                    res = s[left: right+1]

                if s[left] in my_hash:
                    my_hash[s[left]] += 1

                    if my_hash[s[left]] > 0:
                        found -= 1

                left += 1

        return res
        