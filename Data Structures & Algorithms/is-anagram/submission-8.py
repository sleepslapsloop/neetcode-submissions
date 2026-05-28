class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s0, s1, s2, s3 = False, False, False, False

        #s0
        s0 = len(s) == len(t)

        #s1
        hs = defaultdict(int)
        ht = defaultdict(int)

        for char in s:
            hs[char] += 1
        for char in t:
            ht[char] += 1

        s1 = hs == ht

        #s2
        hm = defaultdict(int)

        for char in s:
            hm[char] += 1
        for char in t:
            hm[char] -= 1

        for key, val in hm.items():
            if val != 0:
                s2 = False
        
        s2 = True

        #s3:
        s3 = Counter(s) == Counter(t)

        return s0 and s1 and s2 and s3