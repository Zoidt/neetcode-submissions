class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Mapping character count to list of Anagram

        for s in strs:
            count = [0] * 26 # a - z

            for c in s: 
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()
            
        