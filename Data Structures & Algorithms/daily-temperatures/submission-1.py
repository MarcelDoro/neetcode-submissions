class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            if len(stack) == 0: #Spróbuj zmienić
                stack.append((i, t))
            else:
                while len(stack) != 0 and temperatures[i] > stack[-1][1]: 
                    ind, tem = stack.pop()
                    res[ind] = i - ind
                stack.append((i, t))

        return res