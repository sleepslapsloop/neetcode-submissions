class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True

        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        return False