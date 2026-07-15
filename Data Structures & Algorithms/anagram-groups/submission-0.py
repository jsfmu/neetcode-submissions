from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

    # def groupAnagrams(strs):
    #     res = defaultdict(list)
    #     for s in strs:
    #         # Normalize to lowercase so 'A' and 'a' generate the same key
    #         key = tuple(sorted(s.lower()))
    #         res[key].append(s)
    #     return list(res.values())