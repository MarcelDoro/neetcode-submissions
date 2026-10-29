class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        start = 0
        end = n - 1
        add = numbers[start] + numbers[end]      
          
        while add != target:
            if add < target:
                start += 1
            else:
                end -= 1
            add = numbers[start] + numbers[end]

        return [start + 1, end + 1]


        