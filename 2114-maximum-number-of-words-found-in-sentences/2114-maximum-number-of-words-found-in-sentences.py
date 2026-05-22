class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maxx=0
        for s in sentences:
            maxx=max(maxx,len(s.split()))
        return maxx