import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        h = []
        heapq.heapify(h)
        res = []

        for r in range(len(nums)):
            heapq.heappush(h, [-nums[r], r])
            if r >= k - 1:

                l = r - k + 1
            
                while h[0][1] < l:
                    heapq.heappop(h)
                    
                res.append(-h[0][0])
        return res
            
