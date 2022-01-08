nums = [17,2,33,86,38,41,4,34,91,61,11,81,3,59,29,71,26,44,54,89,46,9,85,62,23,76,45,24,78,14,58,48,57,40,21,49,7,99,8,56,50,19,53,55,10,94,75,68,6,83,84,88,52,80,73,74,79,36,70,28,37,0,42,98,96,92,27,90,47,20,5,77,69,93,31,30,95,25,63,65,51,72,60,16,12,64,18,13,1,35,15,66,67,43,22,87,97,32,39,82]

import math

with open('day4.txt', 'r') as f:
    arr = []
    for line in f.readlines():
        arr.append(line.rstrip())

boards = []

for x in range(0,len(arr),6):
    board = []
    for i in range(5):
        for y in arr[x+i].split(' '):
            if y == '':
                continue
            board.append(int(y))

    boards.append(board)

def evaluate_board(board):
    ticked = [
        [False,False,False,False,False],
        [False,False,False,False,False],
        [False,False,False,False,False],
        [False,False,False,False,False],
        [False,False,False,False,False]
    ]

    for number in nums:
        if number in board:
            ticked[math.floor(board.index(number)/5)][board.index(number)%5] = True
            if isWinning(ticked):
                for line in ticked:
                    print(line)
                return nums.index(number)

def isWinning(a):
    for x in a:
        if False not in x:
            return True

    for y in range(5):
        array = []
        for x in range(5):
            array.append(a[x][y])

        if False not in array:
            return True

    return False


evaluate_board(boards[43])
#for board in boards:
    #evaluate_board(board)
    #if evaluate_board(board) > maximum:
        #maximum = evaluate_board(board)
        #index = boards.index(board)




