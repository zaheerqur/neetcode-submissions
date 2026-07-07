class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}  # tuple of 26 counts -> list of anagram strings
        
        for s in strs:
            count = [0] * 26  # array of 26 zeros
            
            for c in s:
                count[ord(c) - ord('a')] += 1  # increment count at right position
            
            key = tuple(count)  # convert list to tuple so it can be a dict key
            
            if key not in results:
                results[key] = []  # create empty list for this key
            
            results[key].append(s)  # add string to its anagram group
        
        return list(results.values())  # return all the groups