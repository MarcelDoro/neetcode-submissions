class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counts1 = {}
        for i in range(len(s1)):
            if s1[i] not in counts1:
                counts1[s1[i]] = 1
            else:
                counts1[s1[i]] += 1
            
        counts2 = {}
        for i in range(len(s1)):
            if s2[i] not in counts2:
                counts2[s2[i]] = 1
            else:
                counts2[s2[i]] += 1

        for i in range(len(s2) - len(s1)):
            if counts1 == counts2:
                return True

            counts2[s2[i]] -= 1
            if counts2[s2[i]] == 0:
                del counts2[s2[i]]
            if s2[i + len(s1)] not in counts2:
                counts2[s2[i+ len(s1)]] = 1
            else:
                counts2[s2[i + len(s1)]] += 1

        return counts1 == counts2