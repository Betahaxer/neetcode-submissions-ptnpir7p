class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set()
        for num in nums:
            numsSet.add(num)
        maxLength = 0
        for num in numsSet:
            if (num - 1) in numsSet:
                continue
            current = num + 1
            length = 1
            while current in numsSet:
                length += 1
                current += 1
            maxLength = max(maxLength, length)
        return maxLength