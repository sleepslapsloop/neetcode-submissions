class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        temp = self.hashmap[key]

        left, right = 0, len(temp) - 1
        val = None

        while left <= right:
            mid = (left + right) // 2

            if temp[mid][1] == timestamp:
                return temp[mid][0]

            if temp[mid][1] < timestamp:
                val = temp[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return val if val is not None else ""