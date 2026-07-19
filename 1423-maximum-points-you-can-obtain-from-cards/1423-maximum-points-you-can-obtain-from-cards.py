class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum=sum(cardPoints[:k])
        rsum=0
        summ=lsum
        rindex=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[rindex]
            rindex-=1
            summ=max(summ,lsum+rsum)
        return summ

            