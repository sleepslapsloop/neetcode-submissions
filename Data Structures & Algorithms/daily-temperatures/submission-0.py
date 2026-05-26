class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack: List[(int, int)] = [] #(temp, ind)

        for i, temp in enumerate(temperatures):

            while len(stack) != 0 and temp > stack[-1][0]:
                tem, index = stack.pop()
                res[index] = i - index
            stack.append((temp, i))

        return res