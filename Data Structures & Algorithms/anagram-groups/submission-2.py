class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for strn in strs:
            key = [0] * 26
            for char in strn:
                key[ord(char) - ord('a')] += 1
            hashmap[tuple(key)].append(strn)

        return list(hashmap.values())
            