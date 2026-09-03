class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):
            if text1[0] == text2[i]:
                dp[0][i] = 1
                for j in range(i + 1, m):
                    dp[0][j] = 1
                break

        for i in range(n):
            if text1[i] == text2[0]:
                dp[i][0] = 1
                for j in range(i + 1, n):
                    dp[j][0] = 1
                break

        for i in range(1, n):
            for j in range(1, m):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n - 1][m - 1]
