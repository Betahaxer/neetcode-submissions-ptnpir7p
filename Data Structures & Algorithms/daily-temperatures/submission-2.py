class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack = []
        # res = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     while stack and temperatures[stack[-1]] < temperatures[i]:
        #         current_index = stack.pop()
        #         res[current_index] = i - current_index
        #     stack.append(i)
        # return res
        n = len(temperatures)
        res = [0] * n
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:                    
                    break
                j += res[j]
            if temperatures[j] > temperatures[i]:
                res[i] =  j - i
        return res
