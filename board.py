from colors import *
from modules import *
from player import *
from background import *


def Move():
    for i in range(19, 0, -1):
        if(M.y < 10):
            for j in range(50, 0, -1):
                if(board[i][j] == "->"):
                    if(board[i][j + 1] == '  '):
                        board[i][j + 1] = '->'
                    elif(board[i][j + 1] == alien[M.level]):
                        board[i][j + 1] = '  '
                        M.points = M.points + 50
                    board[i][j] = '  '
        elif(M.y > 125):
            for j in range(165, 115, -1):
                if(board[i][j] == "->"):
                    board[i][j] = '  '
                    if(board[i][j + 1] == alien[M.level]):
                        board[i][j + 1] = '  '
                        M.points = M.points + 50
                    elif(board[i][j + 1] == '  '):
                        board[i][j + 1] = '->'
        else:
            for j in range(M.y + 40, M.y - 10, -1):
                if(board[i][j] == "->"):
                    board[i][j] = '  '
                    if(board[i][j + 1] == alien[M.level]):
                        board[i][j + 1] = '  '
                        M.points = M.points + 50
                    elif(board[i][j + 1] == '  '):
                        board[i][j + 1] = '->'


def Print():
    os.system('clear')
    for i in range(2):
        print("", end='\n')
    print('\tPoints = ', end='')
    print(M.points, end='\t\t')
    print('Level = ', end='')
    print(M.level, end='\t\t')
    print('Life = ', end='')
    print(M.life, end='\t')
    print('Time = ', end='')
    print(M.time, end='\n')
    print("", end='\n')
    for i in range(3):
        print(" ", end='')
    for i in range(0, 52):
        print('\x1b[0;30;44m' + "  " + '\x1b[0m', end="")
    for i in range(0, 20):
        print("", end='\n')
        print(" ", end='')
        print(" ", end='')
        print(" ", end='')
        print('\x1b[0;30;44m' + "  " + '\x1b[0m', end="")
        if(M.y < 10):
            for j in range(0, 50):
                if(board[i][j] == "XX"):
                    print(pcolour[M.bullet] + board[i][j], end='')
                else:
                    print(board[i][j], end='')
            print('\x1b[0;30;44m' + "  " + '\x1b[0m', end="")
        elif(M.y > 125):
            for j in range(115, 165):
                if(board[i][j] == "XX"):
                    print(pcolour[M.bullet] + board[i][j], end='')
                else:
                    print(board[i][j], end='')
            print('\x1b[0;30;44m' + "  " + '\x1b[0m', end="")
        else:
            for j in range(M.y - 10, M.y + 40):
                if(board[i][j] == "XX"):
                    print(pcolour[M.bullet] + board[i][j], end='')
                else:
                    print(board[i][j], end='')
            print('\x1b[0;30;44m' + "  " + '\x1b[0m', end="")
    print("", end='\n')
    for i in range(3):
        print(" ", end='')
    for i in range(0, 52):
        print('\x1b[0;30;44m' + "  " + '\x1b[0m', end="")
    print(end='\n')
