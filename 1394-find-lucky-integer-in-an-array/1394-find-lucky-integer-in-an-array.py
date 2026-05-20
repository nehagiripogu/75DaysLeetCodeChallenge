class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq={}
        res=-1
        for num in arr:
            freq[num]=freq.get(num,0)+1
        for num,val in freq.items():
            if num==val:
                res=max(res,num)
        return res