class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_hash = dict()
        max_len, left, right = 0, 0, 1

        for i, ch in enumerate(s):
            if ch in my_hash and my_hash[ch] >= left:
                left = my_hash[ch] + 1
            max_len = max(max_len, right - left)
            my_hash[ch] = i
            right += 1

        return max_len