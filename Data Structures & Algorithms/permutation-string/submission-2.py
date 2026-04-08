class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        window_count = [0] * 26
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
        for i in range(len(s1)):
            window_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_count[i] == window_count[i]:
                matches += 1
    
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[i]) - ord('a')
            window_count[index] += 1
            if window_count[index] == s1_count[index]:
                matches += 1
            elif window_count[index] == s1_count[index] + 1:
                matches -= 1
            
            left_index = ord(s2[i - len(s1)]) - ord('a')
            window_count[left_index] -= 1
            if window_count[left_index] == s1_count[left_index]:
                matches += 1
            elif window_count[left_index] == s1_count[left_index] - 1:
                matches -= 1
        return matches == 26