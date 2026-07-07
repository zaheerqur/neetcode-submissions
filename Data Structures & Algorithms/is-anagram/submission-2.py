class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## if lengths are unequal, string unequal
        if len(s) != len(t): 
            return False
        
        ## the lenghts have to be equal now -> len(s) = len(t)
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        ## checking the count of each key against each other
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True