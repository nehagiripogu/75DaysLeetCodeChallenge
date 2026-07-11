class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=''
        left=0
        right=0
    
        while left<len(word1) and right<len(word2):
            res+=(word1[left])
            res+=(word2[right])
            left+=1
            right+=1
        res+=word1[left:]
        res+=word2[right:]
        return res