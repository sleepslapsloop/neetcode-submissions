class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def time(arr, k):
            t = 0
            for num in arr:
                t += math.ceil(num / k)
            return t

        kmax = max(piles)
        kmin = 1
        k = kmax

        while kmin <= kmax:
            mid = (kmin + kmax) // 2
            t = time(piles, mid)

            if t <= h:
                k = mid
                kmax = mid - 1
            else:
                kmin = mid + 1

        return k