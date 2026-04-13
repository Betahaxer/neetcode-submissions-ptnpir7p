class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", "}":"{", "]":"["}
        for char in s:
            if stack and char in pairs.keys() and pairs[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return stack == []
                
                