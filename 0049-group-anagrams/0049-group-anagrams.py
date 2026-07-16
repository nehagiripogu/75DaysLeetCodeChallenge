class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        res=[]
        for i in strs:
            ans=[]
            ch="".join(sorted(i))
            if ch not in freq:
                freq[ch]=[]
            freq[ch].append(i)
        return list(freq.values())