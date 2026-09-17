class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i in range(len(heights)):
            
            curr = heights[i]

            while stack and curr < stack[-1][1]:

                top = stack.pop()
                if not stack:
                    left_b = -1
                else:
                    left_b = stack[-1][0]
                right_b = i
                width = right_b - left_b - 1

                area = max(area,width*top[1])

            stack.append([i,curr])
        
        while stack:
            top = stack.pop()
            right_b = len(heights)

            if not stack:
                    left_b = -1
            else:
                left_b = stack[-1][0]
            
            width = right_b - left_b - 1
            area = max(area,width*top[1])

        return area


                