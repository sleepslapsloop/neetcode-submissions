class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hm:
                return sorted([i, hm[diff]])
            else:
                hm[num] = i
                continue
        return list() 