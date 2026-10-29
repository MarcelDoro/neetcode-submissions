class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}
        for c in s1:
            if c not in counts1:
                counts1[c] = 1
            else:
                counts1[c] += 1

        for i in range(len(s2)- len(s1) + 1): #+1?
            counts2 = {}
            for j in range(i, i + len(s1)):               
                if s2[j] not in counts2:
                    counts2[s2[j]] = 1
                else:
                    counts2[s2[j]] += 1
            if counts1 == counts2:
                return True
        
        return False
            


