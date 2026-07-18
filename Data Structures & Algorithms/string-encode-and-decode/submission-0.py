class Solution:
        # Define the relationship
            # String --> List of strings
        # Look at inputs
            # What limits the input?
            # Nothing, the string is supposed to be encoded
        # Look at outputs
            # What limits the output?
            # Each string has to be exact to the original list
        # Building variables around s and strs to choke the algorithm's space and time complexity
            
    def encode(self, strs: List[str]) -> str:
        # return "".join(f"{len(s)}#{s}" for s in strs)
        res = []
        for s in strs:
            res.extend(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            word_len = int(s[i:j])
            i = j + 1
            j = i + word_len
            res.append(s[i:j])
            i = j

        return res