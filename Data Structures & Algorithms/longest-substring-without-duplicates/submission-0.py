class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lookup = set()
        left = 0
        maxLen = 0

        for right in range(len(s)):

            while s[right] in lookup:
                lookup.discard(s[left])
                left += 1

            lookup.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen