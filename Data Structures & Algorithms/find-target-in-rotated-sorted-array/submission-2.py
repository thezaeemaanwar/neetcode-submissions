class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, mid, right = 0, None, len(nums) - 1

        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid

            if (nums[mid] >= nums[left] and (target > nums[mid] or target < nums[left])) or (nums[mid] <= nums[left] and nums[mid] < target and target <= nums[right]):
                left = mid + 1
            else:
                right = mid

        if left == right and nums[left] == target:
            return left

        return -1