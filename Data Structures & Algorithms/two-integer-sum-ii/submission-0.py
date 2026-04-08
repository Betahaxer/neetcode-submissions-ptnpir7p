class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            print(current)
            if target == current:
                return [left + 1, right + 1]
            elif target > current:
                left += 1
            else:
                right -= 1
        return [0, 0]