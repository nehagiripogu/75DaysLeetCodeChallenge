class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * n
        stack = []  # store indices
        
        for i in range(2 * n):
            while stack and nums[i % n] > nums[stack[-1]]:
                result[stack.pop()] = nums[i % n]
            
            if i < n:
                stack.append(i)
        
        return result