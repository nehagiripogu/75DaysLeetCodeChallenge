class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        subset=[]
        def backtrack(start,remaining):
            if remaining==0:
                res.append(subset[:])
                return
            if remaining <0:
                return
            for i in range(start,len(candidates)):
                subset.append(candidates[i])
                backtrack(i,remaining-candidates[i])
                subset.pop()
        backtrack(0,target)
        return res