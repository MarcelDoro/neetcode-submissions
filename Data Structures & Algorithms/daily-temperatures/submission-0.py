class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            j = i + 1
            exist = False
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    result.append(j - i)
                    exist = True
                    break
                j += 1
                
            if exist == False:
                result.append(0)

        return result