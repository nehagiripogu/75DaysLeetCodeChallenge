class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new=sorted(set(arr))
        res={}
        ans=[]
        for i , num in enumerate(new):
            res[num]=i+1
        for arr in arr:
            ans.append(res[arr])
        return ans

