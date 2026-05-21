class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        hashmap: dict[str, int] = defaultdict(int)

        for c1 in s:
            hashmap[c1] += 1

        for c2 in t:
            hashmap[c2] -= 1

        for val in hashmap.values():
            if val != 0:
                return False

        return True