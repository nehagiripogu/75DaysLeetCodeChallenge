class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res=[]
        subset=[]
        def backtrack(start,remaining):
            if remaining==0:
                res.append(subset[:])
                return
            if remaining <0:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                subset.append(candidates[i])
                backtrack(i+1,remaining-candidates[i])
                subset.pop()
        backtrack(0,target)
        return res