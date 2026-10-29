class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        #Validate rows
        for i in range(n):            
            count = {}
            for char in board[i]:
                if char not in count:
                    count[char] = 1
                else:
                    count[char] += 1
            
            for k, v in count.items(): #być może na odwrót
                if k != '.' and v > 1:
                    return False

        #Validate collumns
        for i in range(n):
            count = {}
            for j in range(n):
                if board[j][i] not in count:
                    count[board[j][i]] = 1
                else:
                    count[board[j][i]] += 1
            
            for k, v in count.items(): #być może na odwrót
                if k != '.' and v > 1:
                    return False

        #Validate squares
        for i in range(1,8,3):    
            for j in range(1,8,3):
                count = {}   
                min_i = i - 1               
                while min_i <= i + 1:
                    min_j = j - 1
                    while min_j <= j + 1:
                        if board[min_i][min_j] not in count:
                            count[board[min_i][min_j]] = 1
                        else:
                            count[board[min_i][min_j]] += 1
                        min_j += 1
                    min_i += 1
                
                print(count)
                for k, v in count.items(): #być może na odwrót
                    if k != '.' and v > 1:
                        return False
                    
        return True