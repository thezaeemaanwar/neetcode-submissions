class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      nums.sort()
      res = []

      for i in range(len(nums)):
          left, right = i + 1, len(nums) - 1

          if i > 0 and nums[i] == nums[i-1]:
              continue

          while left < right:
              if nums[i] + nums[left] + nums[right] == 0:
                  res.append([nums[i], nums[left], nums[right]])
                  left += 1
                  right -= 1
                  while left <= len(nums) - 1 and left > 0 and nums[left] == nums[left-1]:
                    left += 1
                  while right <= len(nums) - 2 and right > 0 and nums[right] == nums[right+1]:
                    right -= 1

              elif nums[left] + nums[right] > -nums[i]:
                  right -= 1

              else:
                  left += 1

      return res