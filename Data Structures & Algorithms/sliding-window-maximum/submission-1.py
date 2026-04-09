class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # heap solution
        # import heapq

        # heap = []
        # res = []
        # for i in range(len(nums)):
        #     heapq.heappush(heap, (-nums[i], i))
        #     if i >= k - 1:
        #         while heap[0][1] < i - k + 1:
        #             heapq.heappop(heap)
        #         res.append(-heap[0][0])
        # return res

        # dp solution
        n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n
        leftMax[0] = nums[0]
        rightMax[n - 1] = nums[n - 1]

        for i in range(1, len(nums)):
            if i % k == 0:
                leftMax[i] = nums[i]
            else:
                leftMax[i] = max(leftMax[i - 1], nums[i])

            r = len(nums) - 1 - i
            
            if r % k == 0:
                rightMax[r] = nums[r]
            else:
                rightMax[r] = max(rightMax[r + 1], nums[r])
        
        res = [0] * (len(nums) - k + 1)

        for i in range(len(nums) - k + 1):
            res[i] = max(rightMax[i], leftMax[i + k - 1])
        return res
 