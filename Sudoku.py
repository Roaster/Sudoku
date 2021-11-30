import random 
class SudokuPuzzle:
    def __init__(self):
        startingPuzzle = [[x for x in range(1,10)] for row in range(9)]
        for row in range(1,9): 
            startingPuzzle[row] = list(startingPuzzle[row - 1])
            startingPuzzle[row].append(startingPuzzle[row].pop(0))
        self.puzzle = startingPuzzle


    def printPuzzle(self):
        for row in range(9):
            for column in range(9):
                if column % 3 == 0 and column != 0:
                    print("| ", end='')
                print(self.puzzle[row][column], end=' ')
            if row ==2 or row == 5:
                print("\n", "-"*20)
            else:
                print()

    def check(self):
        #check rows
        puzzle = self.puzzle
        for row in range(9):
            foundNums = set()
            for column in range(9):
                if puzzle[row][column] not in foundNums:
                    foundNums.add(puzzle[row][column])
                else:
                    return false

        #check columns
        for column in range(9):
            foundNums = set()
            for row in range(9):
                if puzzle[row][column] not in foundNums:
                    foundNums.add(puzzle[row][column])
                else:
                    return false
            
        return True

        
myPuzzle = SudokuPuzzle()
myPuzzle.printPuzzle()
print(myPuzzle.check())