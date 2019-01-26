#!/usr/bin/python
# -*- coding: utf-8 -*-

from modules import *
from player import *
from colors import *
from board import *

if M.sound == 1:
    os.system('spd-say -tchild_female "Welcome To The World Of Mario"')


def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [],
                                                     [])


setup()
Print()
old_settings = termios.tcgetattr(sys.stdin)
start = time.time()
counter = 0
begin = time.time()
try:
    tty.setcbreak(sys.stdin.fileno())
    while 1:
        t0 = time.time() - start
        if (time.time() - begin > 1):
            M.time = M.time - 1
            begin = time.time()
        if (t0 * 20) % 1 < 0.0001 and (t0 * 20) % 1 > - \
                0.0001 and M.jump == 1 and counter < 8:
            counter = counter + 1
            board[M.x][M.y] = '  '
            M.up()
            board[M.x][M.y] = 'XX'
            Print()
            if counter == 8:
                M.jump = -1
                counter = 0

        if (t0 * 10) % 1 < 0.0001 and (t0 * 10) % 1 > -0.0001 and M.x < 19:
            board[M.x][M.y] = '  '
            M.down()
            board[M.x][M.y] = 'XX'
            Print()
            if(M.x == 18):
                M.jump = 0

        if t0 % 1 < 0.0001 and t0 % 1 > -0.0001:
            for i in ene:
                if board[i.x][i.y] == alien[M.level]:
                    if(board[i.x][i.y + 1] != '  ' or board[i.x + 1][i.y + 1] == '  '):
                        board[i.x][i.y] = '  '
                        i.left()
                        board[i.x][i.y] = alien[M.level]
                    elif (board[i.x][i.y - 1] != '  ' or board[i.x + 1][i.y - 1] == '  '):
                        board[i.x][i.y] = '  '
                        i.right()
                        board[i.x][i.y] = alien[M.level]
                    else:
                        a = random.randint(1, 2)
                        board[i.x][i.y] = '  '
                        if a == 1:
                            i.right()
                        else:
                            i.left()
                        board[i.x][i.y] = alien[M.level]
            Print()

        if M.x == 19 or M.time == 0 or board[M.x +
                                             1][M.y] == '^^' or board[M.x][M.y +
                                                                           1] == alien[M.level] or board[M.x][M.y -
                                                                                                              1] == alien[M.level]:
            M.time = 120
            if M.life > 1:
                if M.sound == 1:
                    os.system('aplay ./sound/death.wav&')
                    time.sleep(0.01)
                Print()
                dec = input('Press Enter To Continue\n')
                M.life = M.life - 1
                M.x = 18
                M.y = 6
                setup()
                board[M.x][M.y] = "XX"
                M.bullet = 0
            else:
                if M.sound == 1:
                    os.system('aplay ./sound/game_over.wav&')
                    time.sleep(0.01)
                Print()
                print(
                    "  ___   _   __ ___ ___    ___ _   _________\n",
                    "/  _| /_\ |  \/  | __|  / _ \ \ / / __| _ \\\n",
                    "| ( |/ _ \| |\/| | |    | () \ V /| _||   /\n",
                    "\___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_\\\n")
                print("YOUR FINAL SCORE - ", end='\t')
                print(M.points, end='\n')

                break
        if M.y == 137 and M.x == 18:
            M.points=M.points+M.time*10
            if M.level == 1:
                if M.sound == 1:
                    os.system('aplay ./sound/stage_clear.wav&')
                    time.sleep(0.1)
                    Print()
                print("CONGRATULATIONS!! LEVEL ONE CLEARED", end='\n')
                dec = input('Press Enter For Next level')
                M.level = 2
                M.x = 18
                M.y = 6
                setup()
                board[M.x][M.y] = "XX"
                M.bullet = 0
            elif M.level == 2:
                if M.sound == 1:
                    os.system('aplay ./sound/stage_clear.wav&')
                    time.sleep(0.01)
                    Print()
                print("CONGRATULATIONS!! LEVEL TWO CLEARED", end='\n')
                dec = input('Press Enter For Next level')
                M.level = 3
                M.x = 18
                M.y = 6
                setup()
                board[M.x][M.y] = "XX"
                M.bullet = 0
            else:
                if M.sound == 1:
                    os.system('aplay ./sound/world_clear.wav&')
                    time.sleep(0.01)
                    Print()
                print("CONGRATULATIONS!! ALL LEVELS CLEARED", end='\n')
                print("YOUR FINAL SCORE - ", end='\t')
                print(M.points, end='\n')
                break
            M.time = 120

        if (t0 * 20) % 5 < 0.0001 and (t0 * 20) % 5 > -0.0001:
            Move()

        if isData():
            c = sys.stdin.read(1)
            if c == 'q':
                break
            if c == 'a':
                board[M.x][M.y] = '  '
                M.left()
                board[M.x][M.y] = 'XX'
                Print()

            if c == ' ':
                if board[M.x][M.y + 1] == '  ' and M.bullet == 1:
                    board[M.x][M.y + 1] = '->'
                if M.sound == 1:
                    print("\a\a")
                Print()

            if c == 'd':
                board[M.x][M.y] = '  '
                M.right()
                board[M.x][M.y] = 'XX'
                Print()
            if c == 'w':
                start = time.time()
                if board[M.x + 1][M.y] != '  ' or M.jump == 0:
                    M.jump = 1
                if M.sound == 1:
                    print("\a")
                Print()
            if c == 's':
                if M.sound == 1:
                    M.sound = 0
                else:
                    M.sound = 1
finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
