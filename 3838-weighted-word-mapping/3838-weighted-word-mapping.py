class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        res=[]
        for word in words:
            total=0
            for ch in word:
                total+=weights[ord(ch)-ord('a')]
            remainder=total%26
            mm=chr(ord('z')-remainder)
            res.append(mm)
        return "".join(res)