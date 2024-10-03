from typing import List
from collections import defaultdict

class Solution:
    """

    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagramGroups[sorted_word].append(word)

        return list(anagramGroups.values())

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams([""]))
print(solution.groupAnagrams(["a"]))