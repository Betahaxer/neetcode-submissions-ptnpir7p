class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for char in s:
            if char.isalnum(): # check if can shortcut the ascii char liddat
                string.append(char)
        string = "".join(string).lower()
        i = 0 
        j = len(string) - 1
        while i <= j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True