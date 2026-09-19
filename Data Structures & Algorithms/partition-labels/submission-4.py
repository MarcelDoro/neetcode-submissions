class Solution:
    def partitionLabels(self, s: str) -> List[int]:        
        last_occur_ind = {}
        for i in range(len(s)):
            last_occur_ind[s[i]] = i

        res = []
        l = 0        
        while l < len(s):
            start = l
            r = last_occur_ind[s[l]]
            while l < r:
                l += 1
                r = max(r, last_occur_ind[s[l]])

            res.append(r - start + 1)
            l += 1

        return res
