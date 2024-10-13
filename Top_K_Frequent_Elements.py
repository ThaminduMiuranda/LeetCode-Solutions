from operator import index
from typing import List

from sympy.solvers.diophantine.diophantine import length


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        frequent = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            frequent[c].append(n)

        result = []

        for i in range(len(frequent)-1, 0, -1):
            for n in frequent[i]:
                result.append(n)
                if len(result) == k:
                    return result

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3],2))
print(solution.topKFrequent([1],1))
print(solution.topKFrequent([1,2,2,3,3,3],2))
print(solution.topKFrequent([7,7],1))
print(solution.topKFrequent([1,2,3,4],1))


