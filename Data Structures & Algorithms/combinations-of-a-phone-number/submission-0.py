class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters: Dict[str, str] = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        res: List[str] = []
        tmp = ''
        def dfs(i):
            nonlocal tmp
            if i >= len(digits):
                res.append(tmp)
                return 

            for d in letters[digits[i]]:
                tmp += d
                dfs(i + 1)
                tmp = tmp[:-1]

        if digits == '':
            return []
        
        dfs(0)
        return res 