class Solution:
    def partition(self, s: str) -> List[List[str]]:        
        def is_palindrome(s: str) -> bool:
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - 1 - i]:
                    return False

            return True

        res: List[List[str]] = []
        tmp: List[int] = []
        def dfs(i: int) -> None:
            if i >= len(s):
                res.append(tmp.copy())
                return 
            
            for j in range(i + 1, len(s) + 1):
                if is_palindrome(s[i:j]) == True:
                    print(s[i:j])
                    tmp.append(s[i:j])
                    dfs(j)
                    tmp.pop()

        dfs(0)
        return res
                
            
