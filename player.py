from colors import *
from modules import *
board = []
ene = []
col = []
col.append('40m')
col.append('41m')
col.append('42m')
col.append('45m')

alien = []
alien.append('ll')
alien.append(OKBLUE + '@@')
alien.append(HEADER + 'oo')
alien.append(RED + '##')

pcolour = []
pcolour.append(YELLOW)
pcolour.append(CYAN)
for i in range(0, 20):
    board.append(["  "] * 170)


class man:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    points = 0
    sound = 1

    def left(self):
        if self.y != 0 and board[self.x][self.y - 1] == '  ':
            self.y = self.y - 1
        elif self.y != 0 and board[self.x][self.y - 1] == YELLOW + "0 ":
            self.y = self.y - 1
            self.points = self.points + 10
            if self.sound == 1:
                os.system('aplay ./sound/coin.wav&')
                time.sleep(0.01)
        elif self.y != 0 and board[self.x][self.y - 1] == CYAN + "$$":
            self.y = self.y - 1
            self.bullet = 1

    def right(self):
        if self.y != 194 and board[self.x][self.y + 1] == '  ':
            self.y = self.y + 1
        elif self.y != 194 and board[self.x][self.y + 1] == YELLOW + "0 ":
            self.y = self.y + 1
            self.points = self.points + 10
            if self.sound == 1:
                os.system('aplay ./sound/coin.wav&')
                time.sleep(0.01)
        elif self.y != 194 and board[self.x][self.y + 1] == CYAN + "$$":
            self.y = self.y + 1
            self.bullet = 1
            if self.sound == 1:
                os.system('aplay ./sound/powerup.wav&')
                time.sleep(0.01)


class player(man):
    def __init__(self, x, y):
        man.__init__(self, x, y)

    life = 3
    level = 1
    bullet = 0
    jump = 0
    time = 120

    def up(self):
        if self.x != 0 and board[self.x - 1][self.y] == '  ':
            self.x = self.x - 1
        elif self.x != 0 and board[self.x - 1][self.y] == YELLOW + "0 ":
            self.x = self.x - 1
            self.points = self.points + 10
            if self.sound == 1:
                os.system('aplay ./sound/coin.wav&')
                time.sleep(0.01)
        elif self.x != 0 and board[self.x - 1][self.y] == YELLOW + "??":
            board[self.x - 1][self.y] = '\x1b[0;30;40m' + "  " + '\x1b[0m'
            board[self.x - 2][self.y] = CYAN + "$$"
            if self.sound == 1:
                os.system('aplay ./sound/powerup_appears.wav&')
                time.sleep(0.01)

        elif self.x != 0 and board[self.x - 1][self.y] == '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m':
            self.x = self.x - 1
            self.jump = -1
            if self.sound == 1:
                os.system('aplay ./sound/brick_smash.wav&')
                time.sleep(0.01)

    def down(self):
        if self.x != 20 and board[self.x + 1][self.y] == '  ':
            self.x = self.x + 1

        elif board[self.x + 1][self.y] == alien[M.level]:
            self.x = self.x + 1
            self.points = self.points + 100

        elif self.x != 20 and board[self.x + 1][self.y] == YELLOW + "0 ":
            self.x = self.x + 1
            self.points = self.points + 20
            if self.sound == 1:
                os.system('aplay ./sound/coin.wav&')
                time.sleep(0.01)

        elif self.x != 20 and board[self.x + 1][self.y] == CYAN + "$$":
            self.x = self.x + 1
            self.bullet = 1


class enemy(man):
    def __init__(self, x, y):
        man.__init__(self, x, y)
    alive = 1


M = player(18, 6)
board[M.x][M.y] = "XX"
