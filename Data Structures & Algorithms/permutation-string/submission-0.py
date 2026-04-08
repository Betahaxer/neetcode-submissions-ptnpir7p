from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = defaultdict(int)
        for char in s1:
            s1_count[char] += 1
        s2_count = defaultdict(int)
        l, r = 0, 0
        while r < len(s2):
            s2_count[s2[r]] += 1
            r += 1
            if s2_count == s1_count:   # check after adding
                return True
            if r - l == len(s1):       # correct window size
                s2_count[s2[l]] -= 1
                if s2_count[s2[l]] == 0:
                    del s2_count[s2[l]]  # keep dicts clean for comparison
                l += 1
        return False
                