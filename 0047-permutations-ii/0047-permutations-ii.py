from itertools import permutations

class Solution(object):
    def permuteUnique(self, nums):
        return [list(p) for p in set(permutations(nums))]