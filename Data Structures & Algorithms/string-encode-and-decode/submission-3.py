class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for string in strs:
            result.append(str(len(string)))
            result.append("#")
            result.append(string)
        return "".join(result)
    def decode(self, s: str) -> List[str]:
        i = 0
        length = []
        stringLength = 0
        result = []
        while(i < len(s)):
            if s[i] == "#":
                stringLength = int("".join(length))
                result.append(s[i + 1 : i + stringLength + 1])
                length = []
                i += stringLength + 1
            else:
                length.append(s[i])
                i += 1
        return result


