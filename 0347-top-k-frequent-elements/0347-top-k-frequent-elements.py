from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums) 
        res=[]
        for key,val in freq.most_common(k):
            res.append(key)
        return res