class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}
        for c1,c2 in zip(s,t):
            if c1 in dict1:
                if dict1[c1]!=c2:
                    return False
            else:
                dict1[c1]=c2
            if c2 in dict2:
                if dict2[c2]!=c1:
                    return False
            else:
                dict2[c2]=c1
        return True
