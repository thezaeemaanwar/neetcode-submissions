class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_hash = {}
        result = 0

        left, maxi = 0, 0

        for right, ch in enumerate(s):
            my_hash[ch] = 1 + my_hash.get(ch, 0)
            maxi = max(maxi, my_hash[ch])

            if (right - left + 1) - maxi > k:
                my_hash[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        
        return result
        