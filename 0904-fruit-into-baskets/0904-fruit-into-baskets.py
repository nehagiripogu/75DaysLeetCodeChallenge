from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left=0
        n=len(fruits)
        maxx=0
        freq=defaultdict(int)
        for right in range(n):
            freq[fruits[right]]+=1
            while len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                
                left+=1
            maxx=max(maxx,right-left+1)
                
        return maxx
