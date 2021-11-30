import random 
#random.seed(10)
class SudokuPuzzle:
    def __init__(self):
        startingPuzzle = [[x for x in range(1,10)] for row in range(9)]
        for row in range(1,9): 
            startingPuzzle[row] = list(startingPuzzle[row - 1])
            startingPuzzle[row].append(startingPuzzle[row].pop(0))

        startingPuzzle = [[0,1,0,8,0,0,4,7,0],
                            [4,7,0,0,3,5,0,2,0],
                            [0,0,2,0,0,0,0,0,0],
                            [0,8,0,0,4,0,0,3,0],
                            [0,0,5,0,8,6,0,0,0],
                            [0,0,3,2,0,0,0,8,0],
                            [0,6,0,0,0,0,7,0,0],
                            [1,0,0,6,5,0,9,0,0],
                            [0,3,9,7,2,0,0,0,0]]

        self.puzzle = startingPuzzle

    def randomize(self):
        for row in range(9):
            randomNumber = int(random.randint(4,8))
            randomIndices = random.sample(range(0,9),randomNumber)
            for index in randomIndices:
                self.puzzle[row][index] = 0
            
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

    def check(self, puzzle):
        
        #check rows
        for row in range(9):
            foundNums = set()
            for column in range(9):
                if puzzle[row][column] == 0:
                    continue
                if puzzle[row][column] not in foundNums:
                    foundNums.add(puzzle[row][column])
                else:
                    #print(row,column)
                    return False

        #check columns
        for column in range(9):
            foundNums = set()
            for row in range(9):
                if puzzle[row][column] == 0:
                    continue
                if puzzle[row][column] not in foundNums:
                    foundNums.add(puzzle[row][column])
                else:
                    return False
        
        #check boxes
        # box1 = puzzle[0:3][0:3]
        # box2 = puzzle[0:3][3:6]
        # box3 = puzzle[0:3][6:9]
        # box4 = puzzle[3:6][0:3]
        # box5 = puzzle[3:6][3:6]
        # box6 = puzzle[3:6][6:9]
        # box7 = puzzle[6:9][0:3]
        # box8 = puzzle[6:9][3:6]
        # box9 = puzzle[6:9][6:9]
        # print(box1)
        # boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]
        # for box in boxes:
        #     foundNums = set()
    
        #     for row in range(3):
        #         for column in range(3):
        #             print(box[row][column])
        #             if box[row][column] not in foundNums and box[row][column] != 0:
        #                 print(box[row][column])
        #                 foundNums.add(box[row][column])
                        
        #             elif box[row][column] == 0:
        #                 continue
        
        #             else: 
        #                 print("returning false", row)
        #                 return False
            
        return True

    def checkValidMove(self, row, column, number):
        
        copyPuzzle = [row[:] for row in self.puzzle]
        copyPuzzle[row][column] = number

        #print(copyPuzzle, self.puzzle)
        return self.check(copyPuzzle)

    def solve(self):
        
        openSpots = []
        for row in range(9):
            for column in range(9):
                if self.puzzle[row][column] == 0:
                    openSpots.append((row,column))
        if openSpots == []:
            return True
        
        
        for index in openSpots:
            for number in range(1,10):
                if self.checkValidMove(index[0], index[1], number):
                    self.puzzle[index[0]][index[1]] = number
                    if(self.solve()): #puzzle
                        return True
                    self.puzzle[index[0]][index[1]] = 0
                
            return False
        
myPuzzle = SudokuPuzzle()
#myPuzzle.printPuzzle()

#print(myPuzzle.check(myPuzzle.puzzle))
#myPuzzle.randomize()

#print("Random Puzzle: ")
myPuzzle.printPuzzle()
#print(myPuzzle.checkValidMove(0,0,1))
print(myPuzzle.solve()) # yPuzzle.puzzle
print("\nSolved Puzzle: ") 
myPuzzle.printPuzzle()
#print(myPuzzle.check())