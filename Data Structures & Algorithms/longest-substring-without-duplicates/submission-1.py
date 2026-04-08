class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        l, r = 0, 1
        longestLength = 0
        while r < len(s):
            while s[r] in s[l:r]:
                l += 1
            longestLength = max(longestLength, r - l + 1)
            r += 1
        return longestLength


        