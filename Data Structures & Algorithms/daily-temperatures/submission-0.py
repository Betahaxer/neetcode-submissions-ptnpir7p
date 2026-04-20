class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            print(stack)
            if not stack or temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    current_index = stack.pop()
                    res[current_index] = i - current_index
                stack.append(i)
        return res
