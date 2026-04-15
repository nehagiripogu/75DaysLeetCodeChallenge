class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nge = {}  # next greater element map
        
        # Step 1: process nums2
        for num in nums2:
            while stack and num > stack[-1]:
                nge[stack.pop()] = num
            stack.append(num)
        
        # remaining elements → no next greater
        while stack:
            nge[stack.pop()] = -1
        
        # Step 2: build result
        return [nge[num] for num in nums1]