class Solution:
    def romanToInt(self, s: str) -> int:
        conversions = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        """
        str -> XXIX = 29, len(s) = 4
        i = 0, 
        i = 1
        i = 2
        i = 3
        """
        answer = 0
        for i in range(len(s)):
            if i + 1 < len(s) and conversions[s[i]] < conversions[s[i + 1]]:
                answer -= conversions[s[i]]
            else:
                answer += conversions[s[i]]
        return answer
