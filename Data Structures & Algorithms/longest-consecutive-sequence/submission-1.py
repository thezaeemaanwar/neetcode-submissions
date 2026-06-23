class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        res = 0

        for num in nums:
            if num in hash_set and num - 1 not in hash_set:
                curr = num
                count = 0

                while int(curr) in hash_set:
                    curr += 1
                    count += 1
            
                res = max (res, count)

        return res
        