class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxvol = 0
        l = 0
        r = len(heights)-1

        while l<r:
            vol = (r-l) * min(heights[l],heights[r])
            maxvol = max(vol,maxvol)
            
            if heights[l] <= heights[r]:
                l += 1
                continue

            if heights[l] >= heights[r]:
                r -= 1
                continue

        return maxvol
         