class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(strn)) + "#" + strn for strn in strs])

    def decode(self, s: str) -> List[str]:
        size = ""
        result, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = s[i:j]
            length = int(length)
            result.append(s[j + 1 : j + length + 1])
            i = j + 1 + length
        
        return result