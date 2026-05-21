class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for j, num1 in enumerate(nums):
                if num1 + num == target and i != j:
                    return sorted([i, j])
        return []