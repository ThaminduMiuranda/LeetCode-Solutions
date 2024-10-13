class Solution:

    def encode(self, strs):
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"

        return res


    def decode(self, str):

        result,i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            result.append(str[j+1 : j+1 + length])
            i = j + 1 + length

        return result


solution = Solution()
original = ["Hello", "World"]
encoded = solution.encode(original)
decoded = solution.decode(encoded)
print(original)
print(encoded)
print(decoded)
