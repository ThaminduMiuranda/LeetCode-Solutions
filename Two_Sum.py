from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = []

        for i in range(len(nums)):
            complement = target - nums[i]
            if(complement in nums and nums.index(complement)!=i):
                indexes.append(i)
                indexes.append(nums.index(complement))
                return indexes

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4], 6))
print(solution.twoSum([3,3], 6))