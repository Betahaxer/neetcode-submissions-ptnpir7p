from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if len(s) < len(t):
        #     return ""
        t_count = defaultdict(int)
        window_count = defaultdict(int)
        for i in range(len(t)):
            t_count[t[i]] += 1
        
        l = 0
        have, need = 0, len(t_count)
        res = [-1, -1]
        resLength = float("infinity")
        for r in range(len(s)):
            window_count[s[r]] += 1
            if window_count[s[r]] == t_count[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLength:
                    res[0] = l
                    res[1] = r
                    resLength = r - l + 1
                window_count[s[l]] -= 1
                if window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        print(l, r)
        l, r = res
        return "" if resLength == float("Infinity") else s[l:r+1]