class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True

        map1 = dict()
        map2 = dict()
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if c1 not in map1:
                map1[c1] = 1
            else:
                map1[c1] += 1
            if c2 not in map2:
                map2[c2] = 1
            else:
                map2[c2] += 1
            
        return map1 == map2