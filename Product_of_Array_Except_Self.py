from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(len(nums) - 1, -1, -1):
            result[j] *= postfix
            postfix *= nums[j]

        return result

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))
print(solution.productExceptSelf([-1,1,0,-3,3]))
print(solution.productExceptSelf([2,3,5,0]))