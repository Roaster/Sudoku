import random 
import pygame
#random.seed(10)
class SudokuPuzzle:
    def __init__(self):
        
        startingPuzzle = [[x for x in range(1,10)] for row in range(9)]
        for row in range(1,9): 
            startingPuzzle[row] = list(startingPuzzle[row - 1])
            startingPuzzle[row].append(startingPuzzle[row].pop(0))
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

        self.puzzle = startingPuzzle
        self.puzzleBackup = [row[:] for row in startingPuzzle]
        
    def reset(self):
        self.puzzle = [row[:] for row in self.puzzleBackup]
        drawBoard()

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
        box1 = [row[0:3] for row in puzzle[0:3]]
        box2 = [row[0:3] for row in puzzle[3:6]]
        box3 = [row[0:3] for row in puzzle[6:9]]
        box4 = [row[3:6] for row in puzzle[0:3]]
        box5 = [row[3:6] for row in puzzle[3:6]]
        box6 = [row[3:6] for row in puzzle[6:9]]
        box7 = [row[6:9] for row in puzzle[0:3]]
        box8 = [row[6:9] for row in puzzle[3:6]]
        box9 = [row[6:9] for row in puzzle[6:9]]
        
        boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9]

        for box in boxes:
            foundNums = set()
            for row in range(3):
                for column in range(3):
                    #print(box[row][column])
                    if box[row][column] not in foundNums and box[row][column] != 0:
                        #print(box[row][column])
                        foundNums.add(box[row][column])
                    elif box[row][column] == 0:
                        continue
                    else: 
                        #print("returning false", row)
                        return False
            
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
                    drawBoard()
                    if(self.solve()): #puzzle
                        return True
                    self.puzzle[index[0]][index[1]] = 0
            return False
        


def drawBoard():
    w = 70
    x, y = 0, 0
    for j in range(9):
        for i in range(9):
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(x, y, w, w))
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(x+2, y+2, w-1, w-1))
            if i != 9 and j != 9:
                number_image = number_font.render( str(myPuzzle.puzzle[j][i]), True, WHITE, BLACK )
                number_imageRect = number_image.get_rect()
                screen.blit(number_image, (x+20,y+10))
                # if j == 2 and i == 2:
                #     number_image = number_font.render( "5", True, BLACK, WHITE )
                #     # number_imageRect = number_image.get_rect()
                #     # number_imageRect.center = (x, y)
                #     screen.blit(number_image, (x,y))
            x = x + w
        y = y + w
        x = 0
        
        pygame.display.flip()

myPuzzle = SudokuPuzzle()
myPuzzle.printPuzzle()
pygame.init()
size = 630,800
screen = pygame.display.set_mode(size)
number_font = pygame.font.SysFont( None, 90 )
Play = True

BLACK = (0,0,0)
WHITE = (255, 255, 255)
move = ""

drawBoard()
clock = pygame.time.Clock()
while Play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Play = False
            print("Ending")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                myPuzzle.solve()
            if event.key == pygame.K_r:
                myPuzzle.reset()
    if move != "":
        print(move[0], move[1], move[2])
        x1 = int(move[0])
        x2 = int(move[1])
        try:
            myPuzzle.puzzle[x1][x2] = int(move[2])
            drawBoard()
        except:
            print("Bad move.")
    
    
    #draw outside borders
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(628, 0,2, 630))
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, 630,630, 3))


    pygame.display.flip()
    clock.tick(5)
    #print("Enter next move")
    #move = input()

pygame.quit()
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
