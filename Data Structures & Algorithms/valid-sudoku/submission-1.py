class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # BRUTE FORCE
        # rows
        for row in board:
            mySet = set()
            for num in row:
                if num == '.':
                    continue
                if num not in mySet:
                    mySet.add(num)
                else:
                    return False
        
        # columns
        for column in range(len(board)):
            mySet = set()
            for row in range(len(board)):
                num = board[row][column]
                if num == '.':
                    continue
                if num in mySet:
                    return False
                else:
                    mySet.add(num)

        # 3x3
        for subBoxRow in range(0,len(board),3):
            for subBoxCol in range(0,len(board),3):
                mySet = set()
                for subRow in range(subBoxRow, subBoxRow+3):
                    for subCol in range(subBoxCol, subBoxCol+3):
                        num = board[subRow][subCol]
                        if num == '.':
                            continue
                        if num in mySet:
                            return False
                        else:
                            mySet.add(num)

        return True



