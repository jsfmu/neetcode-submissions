class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != t:
        #     return False

        # countS = [0]*26
        # countT = [0]*26

        # for i in len(s)
        return Counter(s) == Counter(t)