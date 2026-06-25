class Solution:
    def findMin(self, nums: List[int]) -> int:
        first, last, target = 0, len(nums) - 1, len(nums)//2

        if nums[last] > nums[first]:
            return nums[first]

        while first < last:
            target = (last - first) // 2 + first

            if nums[target] > nums[last]:
                first = target + 1
            else:
                last = target

        return nums[last]
        