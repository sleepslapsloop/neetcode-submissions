class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if len(s) == 0:
            return True
        
        smap: dict[str, int] = defaultdict(int)
        tmap: dict[str, int] = defaultdict(int)

        for c1 in s:
            smap[c1] += 1
        for c2 in t:
            tmap[c2] += 1
        
        return smap == tmap