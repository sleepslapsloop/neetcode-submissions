class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        temp = [(pos, vel) for pos, vel in zip(position, speed)]
        temp = sorted(temp)[::-1]
        stack = []

        for pos, vel in temp:
            time = (target - pos) / vel
            stack.append(time)

            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)