from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq=Counter(s)
        res=0
        odd=0
        for ch in freq:
            if freq[ch]%2==0:
                res+=freq[ch]
            else:
                res+=(freq[ch]//2)*2
                odd+=1
        if odd>=1:
            res+=1
        return res
