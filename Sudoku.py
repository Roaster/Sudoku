import random 
import pygame
import time

#random.seed(10)
class SudokuPuzzle:
    def __init__(self, puzzle):
        
        if puzzle == "":
            startingPuzzle = convertToSudokuFormat(puzzle)
        else:
            #Randomized simple puzzle
            startingPuzzle = [[x for x in range(1,10)] for row in range(9)]
            for row in range(1,9): 
                startingPuzzle[row] = list(startingPuzzle[row - 1])
                startingPuzzle[row].append(startingPuzzle[row].pop(0))
            #Randomized simple puzzle

            #easy puzzle
            #https://www.puzzles.ca/sudoku_puzzles/sudoku_easy_979.html
            #https://www.puzzles.ca/sudoku_puzzles/sudoku_easy_979_solution.html
            startingPuzzle = [[0,1,0,8,0,0,4,7,0],
                                [4,7,0,0,3,5,0,2,0],
                                [0,0,2,0,0,0,0,0,0],
                                [0,8,0,0,4,0,0,3,0],
                                [0,0,5,0,8,6,0,0,0],
                                [0,0,3,2,0,0,0,8,0],
                                [0,6,0,0,0,0,7,0,0],
                                [1,0,0,6,5,0,9,0,0],
                                [0,3,9,7,2,0,0,0,0]]

            #hard puzzle
            #https://www.puzzles.ca/sudoku_puzzles/sudoku_hard_973.html
            #https://www.puzzles.ca/sudoku_puzzles/sudoku_hard_973_solution.html
            # startingPuzzle = [[0,0,0,0,0,0,0,0,0],
            #                     [5,4,8,0,1,0,0,0,0],
            #                     [0,0,0,2,0,4,0,0,0],
            #                     [0,0,0,0,0,0,9,0,0],
            #                     [0,5,0,7,3,0,6,0,4],
            #                     [1,7,0,0,0,0,0,0,3],
            #                     [0,0,9,0,4,0,0,0,0],
            #                     [3,0,0,0,2,8,1,0,0],
            #                     [0,0,0,0,0,0,7,0,9]]


        #This is the puzzle that will be solved in the background
        self.puzzle = startingPuzzle
        #PuzzleBackup is the users puzzle
        self.puzzleBackup = [row[:] for row in startingPuzzle]
        #This is an empty puzzle to reset with
        self.puzzleReset = [row[:] for row in startingPuzzle]
        self.solved = False
        
    def reset(self):
        self.puzzle = [row[:] for row in self.puzzleReset]
        self.puzzleBackup = [row[:] for row in self.puzzleReset]
        self.solved = False
        drawBoard(self.puzzle)

    def hint(self):
        self.solve(display=False)
        for i in range(9):
            for j in range(9):
                if(self.puzzleBackup[i][j] == 0):
                    self.puzzleBackup[i][j] = self.puzzle[i][j]
                    drawBoard(self.puzzleBackup)
                    return

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


    def checkSquare(self, puzzle, row, column, number):
        rowStart = row - row%3
        columnStart = column - column%3
        foundNumbers = set()

        for i in range(3):
            for j in range(3):
                if puzzle[rowStart+i][columnStart+j] not in foundNumbers and puzzle[rowStart+i][columnStart+j] != 0:
                    foundNumbers.add(puzzle[rowStart+i][columnStart+j])
                elif puzzle[rowStart+i][columnStart+j] == 0:
                    continue
                else:
                    return False
        return True

    def checkRow(self, puzzle, row):
        foundNumbers = set()
        for i in range(9):
            if puzzle[row][i] not in foundNumbers and puzzle[row][i] != 0:
                foundNumbers.add(puzzle[row][i])
            elif puzzle[row][i] == 0:
                continue
            else:
                return False
        return True

    def checkColumn(self, puzzle, column):
        foundNumbers = set()
        for i in range(9):
            if puzzle[i][column] not in foundNumbers and puzzle[i][column] != 0:
                foundNumbers.add(puzzle[i][column])
            elif puzzle[i][column] == 0:
                continue
            else:
                return False
        return True

    def updatePosition(self, row, column, number):
        self.puzzleBackup[row][column] = number
        drawBoard(self.puzzleBackup)

        return


    def checkValidMove(self, row, column, number):
        copyPuzzle = [row[:] for row in self.puzzle]
        copyPuzzle[row][column] = number

        if not self.checkSquare(copyPuzzle, row, column, number):
            return False
        if not self.checkRow(copyPuzzle,row):
            return False
        if not self.checkColumn(copyPuzzle,column):
            return False
        return True

    def solve(self, display):
        openSpots = []
        if self.solved:
            return True

        for row in range(9):
            for column in range(9):
                if self.puzzle[row][column] == 0:
                    openSpots.append((row,column))

        if openSpots == []:
            self.solved = True
            return True
        
        for index in openSpots:
            for number in range(1,10):
                if self.checkValidMove(index[0], index[1], number):
                    self.puzzle[index[0]][index[1]] = number
                    if display:
                        drawBoard(self.puzzle)
                    if(self.solve(display)):
                        return True
                    self.puzzle[index[0]][index[1]] = 0
            return False
        
        
def convertToSudokuFormat(puzzle):
    index = 0
    convertedPuzzle = []
    for i in range(9):
        puzzleRow = []
        for j in range(9):
            if puzzle[index] == '.':
                puzzleRow.append(0)
            else: 
                puzzleRow.append(int(puzzle[index]))
            index += 1
        convertedPuzzle.append(puzzleRow)
    
    return convertedPuzzle


def drawBoard(puzzle):
    w = 70
    x, y = 0, 0
    for j in range(9):
        for i in range(9):
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(x, y, w, w))
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(x+2, y+2, w-1, w-1))
            if i != 9 and j != 9:
                puzzleNumber = str(puzzle[j][i])

                if puzzleNumber == "0":
                    puzzleNumber = " "
                number_image = number_font.render(puzzleNumber, True, WHITE, BLACK )
                number_imageRect = number_image.get_rect()
                screen.blit(number_image, (x+20,y+10))
            x = x + w
        y = y + w
        x = 0
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(628, 0,2, 630))
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, 630,630, 3))
        pygame.display.flip()

puzzleString = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
#Testing
myPuzzle = SudokuPuzzle(puzzleString)
myPuzzle.printPuzzle()
print(myPuzzle.checkValidMove(0,5,2))
#Testing


pygame.init()
size = 630,630
screen = pygame.display.set_mode(size)
number_font = pygame.font.SysFont( None, 90 )
BLACK = (0,0,0)
WHITE = (255, 255, 255)

def start():
    move = ""
    Play = True
    drawBoard(myPuzzle.puzzleBackup)
    while Play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Play = False
                print("Ending")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    myPuzzle.solve(True)
                if event.key == pygame.K_r:
                    myPuzzle.reset()
                if event.key == pygame.K_i:
                    print("Enter next move")
                    move = input()
                    row = int(move[0])
                    column = int(move[1])
                    inputNum = int(move[2])
                    if myPuzzle.puzzleBackup[row][column] == 0:
                        myPuzzle.updatePosition(row, column, inputNum)
                
                    
                if event.key == pygame.K_h:
                    myPuzzle.hint()
        
    pygame.quit()

start()
#Testing...

# myPuzzle = SudokuPuzzle()
# myPuzzle.printPuzzle()
#startGame()
#print(myPuzzle.check(myPuzzle.puzzle))
#myPuzzle.randomize()
#print(myPuzzle.checkValidMove(0,0,1))
#print("Random Puzzle: ")
##myPuzzle.printPuzzle()
#print(myPuzzle.checkValidMove(0,0,1))
start = time.time()
print(myPuzzle.solve(False)) # yPuzzle.puzzle
end = time.time()
print(end-start)
#print("\nSolved Puzzle: ") 
myPuzzle.printPuzzle()
#print(myPuzzle.check())

#MIGHT NEED?
# def check(self, puzzle):
    #     #check rows
    #     # for row in range(9):
    #     #     foundNums = set()
    #     #     for column in range(9):
    #     #         if puzzle[row][column] == 0:
    #     #             continue
    #     #         if puzzle[row][column] not in foundNums:
    #     #             foundNums.add(puzzle[row][column])
    #     #         else:
    #     #             #print(row,column)
    #     #             return False

    #     #check columns
    #     for column in range(9):
    #         foundNums = set()
    #         for row in range(9):
    #             if puzzle[row][column] == 0:
    #                 continue
    #             if puzzle[row][column] not in foundNums:
    #                 foundNums.add(puzzle[row][column])
    #             else:
    #                 return False
        
    #     return True
    #     #check boxes
    #     #need more efficient way to check squares
    #     # box1 = [row[0:3] for row in puzzle[0:3]]
    #     # box2 = [row[0:3] for row in puzzle[3:6]]
    #     # box3 = [row[0:3] for row in puzzle[6:9]]
    #     # box4 = [row[3:6] for row in puzzle[0:3]]
    #     # box5 = [row[3:6] for row in puzzle[3:6]]
    #     # box6 = [row[3:6] for row in puzzle[6:9]]
    #     # box7 = [row[6:9] for row in puzzle[0:3]]
    #     # box8 = [row[6:9] for row in puzzle[3:6]]
    #     # box9 = [row[6:9] for row in puzzle[6:9]]
    #     # boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]

        


    #     # boxes = []
    #     # row = 0
    #     # for i in range(9):
    #     #     box = []
    #     #     column = 0
    #     #     for j in range(3):
    #     #         for k in range(9):
    #     #             box.append((row, k))
    #     #         column+=3
    #     #         row +=1
    #     #         boxes.append(box)
    #     #     box = []
    #     #     row = row % 9
    #     # print(boxes)


    #     # for box in boxes:
    #     #     foundNums = set()
    #     #     for row in range(3):
    #     #         for column in range(3):
    #     #             #print(box[row][column])
    #     #             if box[row][column] not in foundNums and box[row][column] != 0:
    #     #                 #print(box[row][column])
    #     #                 foundNums.add(box[row][column])
    #     #             elif box[row][column] == 0:
    #     #                 continue
    #     #             else: 
    #     #                 #print("returning false", row)
    #     #                 return False
            
    #     # return True