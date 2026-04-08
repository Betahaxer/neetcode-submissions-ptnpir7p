class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            numsDict = dict()
            for num in nums:
                numsDict[num] = numsDict.get(num, 0) + 1 
            numsDictSorted = sorted(numsDict, key=lambda x: numsDict[x], reverse=True)
            return numsDictSorted[:k]
