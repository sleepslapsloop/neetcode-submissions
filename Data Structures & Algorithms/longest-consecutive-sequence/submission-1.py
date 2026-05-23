class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        maxLen = 0
        hashset = set(nums)

        for num in hashset:
            if num - 1 not in hashset:
                length = 1
                while num + length in hashset:
                    length += 1
                maxLen = length if length > maxLen else maxLen
        
        return maxLen