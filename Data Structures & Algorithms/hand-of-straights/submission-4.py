class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counter = Counter(hand)

        for card in sorted(counter.keys()):
            if counter[card] > 0:
                amount = counter[card]
                for i in range(card, card + groupSize):
                    if counter[i] < amount:
                        return False

                    counter[i] -= amount

        return True
        