class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i,n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                stackn, stacki = stack.pop()
                res[stacki] = i - stacki
            stack.append((n, i))
        return res