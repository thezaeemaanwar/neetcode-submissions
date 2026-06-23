class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zeroes = 1, 0
        output = [0] * len(nums)

        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                product *= num

        if zeroes > 1:
            return output

        for idx, num in enumerate(nums):
            if zeroes:
                output[idx] = 0 if num else int(product)
            else:
                output[idx] = product // num

        return output