class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        mid = int((left + right) / 2)

        while left <= right:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
                mid = int((left + right) / 2)
            else:
                left = mid + 1
                mid = int((left + right) / 2)

        return -1