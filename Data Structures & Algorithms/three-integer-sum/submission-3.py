class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        result = []
        
        for i, num in enumerate(nums):
            target = -num
            left, right = i + 1, len(nums) - 1

            if i > 0 and nums[i - 1] == nums[i]:
                continue 

            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left - 1] == nums[left]:
                        left += 1

                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1

        return result