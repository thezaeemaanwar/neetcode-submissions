class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict = dict()
        for idx, n in enumerate(nums):
            if target - n in n_dict:
                return [n_dict[target - n], idx]
            else:
                n_dict[n] = idx
        return []
        



        