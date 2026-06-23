class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r_dict = defaultdict(list)
        for m in strs:
            count = [0]*26
            for n in m:
                count[ord(n) - ord('a')] += 1
            r_dict[tuple(count)].append(m)
        return list(r_dict.values())