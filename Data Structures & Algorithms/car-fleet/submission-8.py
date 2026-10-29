class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_spe = []
        for i in range(len(position)):
            pos_and_spe.append((position[i], speed[i]))

        pos_and_spe.sort(key = lambda x: x[0])
        print(pos_and_spe)

        times = []
        for pair in pos_and_spe:
            time = (target - pair[0]) / pair[1]
            times.append(time)

        print(times)
        for i in range(len(times) - 1, 0, -1):
            if times[i - 1] <= times[i]:
                del times[i - 1]
                i -= 1
                
        return len(times)