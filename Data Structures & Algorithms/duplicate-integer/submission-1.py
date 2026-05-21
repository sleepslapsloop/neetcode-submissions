class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = dict()
        for i, num in enumerate(nums):
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
            if hm[num] > 1:
                return True
        return False