class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}

        # count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # find element appearing once
        for key, value in freq.items():

            if value == 1:
                return key