class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        helperStack = []
        n = len(temperatures)
        result = [0] * n
        for idx in range(n - 1, -1, -1):
            while helperStack and temperatures[idx] >= temperatures[helperStack[-1]]:
                helperStack.pop()
            if helperStack:
                result[idx] = helperStack[-1] - idx
            helperStack.append(idx)
        return result
        