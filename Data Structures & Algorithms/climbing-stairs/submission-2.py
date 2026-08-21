class Solution:
    def climbStairs(self, n: int) -> int:
        combinations = [0, 1, 2]

        while len(combinations) <= n:
            num_of_com = combinations[-1] + combinations[-2]
            combinations.append(num_of_com)

        return combinations[n]
