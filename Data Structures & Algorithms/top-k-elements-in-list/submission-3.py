class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm = defaultdict(int)
        temp = [[] for i in range(len(nums) + 1)]
        ans = []
        ind = 0

        for num in nums:
            hm[num] += 1

        for key, val in hm.items():
            temp[val].append(key)

        for arr in temp[::-1]:
            if arr:
                ans.extend(arr)
            if len(ans) >= k:
                break

        return ans