class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def find_from_right(s: str, c: str) -> int | None:
            for i in range(len(s) - 1, -1, -1):
                if s[i] == c:
                    return i

            return None

        
        last_occur_ind = {}
        for c in s:
            last_occur_ind[c] = find_from_right(s, c)

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
