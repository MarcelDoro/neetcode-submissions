class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def find_from_right(s: str, c: str) -> int | None:
            for i in range(len(s) - 1, -1, -1):
                if s[i] == c:
                    return i

            return None


        res = []
        i = 0
        while i < len(s):
            last = find_from_right(s, s[i])            
            substr_end = last
            substr_pre = -1
            while substr_end != substr_pre:
                substr_pre = substr_end
                for j in range(i, substr_end + 1):
                    substr_end = max(substr_end, find_from_right(s, s[j]))                

            res.append(substr_end - i + 1)
            i = substr_end + 1

        return res
        