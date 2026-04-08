class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            length = len(string)
            result += str(length) + "#" + string
        return result

    def decode(self, s: str) -> List[str]:
        i = j = 0
        result = []
        while (i < len(s)):
            if s[j] == "#":
                length = int(s[i:j])
                result.append(s[j + 1:j + 1 + length])
                i = j + 1 + length
                j = i
            j += 1

        return result


            


