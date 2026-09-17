class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = {}

        for num in hand:
            counter[num] = counter.get(num, 0) + 1

        while counter:
            val = min(counter.keys())
            for _ in range(groupSize):
                if val not in counter:
                    return False

                if counter[val] == 1:
                    del counter[val]
                else:
                    counter[val] -= 1

                val += 1

        return True