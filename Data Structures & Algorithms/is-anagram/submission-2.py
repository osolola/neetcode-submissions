class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        freq = defaultdict(int)

        for i in range(len(s)):
            freq[s[i]] += 1
        
        for j in range(len(t)):
            freq[t[j]] -= 1

        if(all(f == 0 for f in freq.values())):
            return True
        else: 
            return False
        
            

        
        

        

        
        