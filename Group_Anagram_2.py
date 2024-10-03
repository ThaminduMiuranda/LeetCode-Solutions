from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
            optimal O(m * n) time complexity
            where
            m is the total number of words
            and
            n is the average length of each word.
        """
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0]*26 # a...z

            for c in s:
                count[ord(c) - ord('a')] += 1 # (a-z=0)  (z-a=25)

                # a = 97 -> 97-97 = 0
                # b = 98 -> 98-97 = 1
                # c = 99 -> 99-97 = 2
                # .
                # .
                # .
                # z = 122 -> 122-97 = 25
                #             |   |
                #             v   v
                #             z   a


            res[tuple(count)].append(s)

        return res.values()

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["a"]))