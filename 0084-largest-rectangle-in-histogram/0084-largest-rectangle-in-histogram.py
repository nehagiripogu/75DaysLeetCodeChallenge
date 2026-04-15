class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []  # store indices
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                
                max_area = max(max_area, h * width)
            
            stack.append(i)
        
        # process remaining stack
        while stack:
            h = heights[stack.pop()]
            
            if stack:
                width = n - stack[-1] - 1
            else:
                width = n
            
            max_area = max(max_area, h * width)
        
        return max_area