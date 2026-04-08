class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArray = [0] * 26
        for char in s:
                sArray[ord(char) - ord('a')] += 1
        for char in t:
            sArray[ord(char) - ord('a')] -= 1
        for elem in sArray:
            if elem != 0:
                return False
        return True
            