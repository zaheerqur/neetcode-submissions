class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## if lengths unequal, automatic disqualification
        if len(s) != len(t):
            return False

        ## at this point, the lengths are the same, len(s) = len(t)
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True