class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsSorted = sorted(nums)
        res = []

        for i, num in enumerate(numsSorted):
            if num > 0:
                break
            if i and num == numsSorted[i - 1]:
                continue
            l, r = i + 1, len(numsSorted) - 1
            while l < r:
                threeSum = num + numsSorted[l] + numsSorted[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, numsSorted[l], numsSorted[r]])
                    l += 1
                    r -= 1
                    while numsSorted[l] == numsSorted[l - 1] and l < r:
                        l += 1
        return res