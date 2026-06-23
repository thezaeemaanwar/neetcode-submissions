class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict()
        freq_table = [[] for i in range(len(nums) + 1)]

        for n in nums:
            res[n] = 1 + res.get(n, 0)
        
        for n, count in res.items():
            freq_table[count].append(n)
        
        result = []
        for i in range(len(freq_table)-1, 0, -1):
            if freq_table[i] != []:
                result.extend(freq_table[i])
                if len(result) >= k:
                    break
        
        return result

