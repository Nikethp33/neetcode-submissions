class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        l = 0
        r = length - 1
        water = 0
        max_l = 0
        max_r = 0

        while (l < r):
            if height[l]<=height[r]:
                max_l= max(max_l,height[l])
                water += max_l - height[l]
                l += 1 
            else:
                max_r= max(max_r,height[r])
                water += max_r - height[r]
                r -= 1
        return water