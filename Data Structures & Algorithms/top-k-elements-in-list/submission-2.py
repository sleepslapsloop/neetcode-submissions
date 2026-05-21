class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr: List[tuple(int, int)] = Counter(nums).most_common(k)
        ans: List[int] = []

        for tup in arr:
            ans.append(tup[0])

        return ans