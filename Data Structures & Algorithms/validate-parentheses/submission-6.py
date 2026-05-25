class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = {'(':')', '[':']', '{':'}'}
        stack = []

        if len(s) % 2 != 0:
            return False

        for char in s:
            if char in hashmap:
                stack.append(char)
            elif not stack or hashmap[stack.pop()] != char:
                return False
            else:
                pass
        
        return len(stack) == 0
            