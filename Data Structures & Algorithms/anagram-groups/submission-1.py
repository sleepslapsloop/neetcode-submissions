class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap: dict[tuple[int], List[str]] = defaultdict(list)

        for strn in strs:
            arrKey: List[int] = [0] * 26

            for char in strn:
                arrKey[ord(char) - ord('a')] += 1
            
            hashmap[tuple(arrKey)].append(strn)

        return list(hashmap.values())