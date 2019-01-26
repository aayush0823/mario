from colors import *
from player import *
base = []
base.append('12m')
base.append('42m')
base.append('43m')
base.append('45m')


def setup():
    board.clear()
    for i in range(0, 20):
        board.append(["  "] * 170)
    for i in range(0, 170):
        board[19][i] = '\x1b[0;30;' + base[M.level] + "  " + '\x1b[0m'
    board[18][1] = '\x1b[0;30;' + col[M.level] + RED + "  " + '\x1b[0m'
    board[17][1] = '\x1b[0;30;' + col[M.level] + RED + "  " + '\x1b[0m'
    board[18][4] = '\x1b[0;30;' + col[M.level] + RED + "  " + '\x1b[0m'
    board[17][4] = '\x1b[0;30;' + col[M.level] + RED + "  " + '\x1b[0m'
    board[16][4] = '\x1b[0;30;' + col[M.level] + RED + "  " + '\x1b[0m'
    board[16][1] = '\x1b[0;30;' + col[M.level] + RED + "  " + '\x1b[0m'
    board[16][3] = '\x1b[0;30;' + col[M.level] + RED + "  " + '\x1b[0m'
    board[16][4] = '\x1b[0;30;' + col[M.level] + RED + "  " + '\x1b[0m'
    board[16][2] = '\x1b[0;30;' + col[M.level] + RED + "  " + '\x1b[0m'
    board[16][1] = '\x1b[0;30;' + col[M.level] + RED + "  " + '\x1b[0m'

    board[15][10] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][11] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][12] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][13] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][14] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][15] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[14][12] = YELLOW + "0 "
    board[14][13] = YELLOW + "0 "

    board[11][13] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][14] = YELLOW + "??"
    board[11][15] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[10][13] = YELLOW + "0 "

    board[18][23] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][23] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][23] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][23] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[14][23] = YELLOW + "0 "

    board[18][27] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][27] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][27] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][27] = YELLOW + "0 "

    board[17][31] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][31] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][31] = YELLOW + "0 "

    board[18][39] = "^^"
    board[18][40] = "^^"
    board[19][39] = "^^"
    board[19][40] = "^^"

    board[15][45] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][46] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][47] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][48] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][49] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][50] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[9][48] = YELLOW + "0 "
    board[8][48] = YELLOW + "0 "
    board[7][48] = YELLOW + "0 "

    board[18][55] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][55] = YELLOW + "0 "
    board[18][56] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][56] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][56] = YELLOW + "0 "
    board[18][57] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][57] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][57] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][57] = YELLOW + "0 "
    board[18][58] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][58] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][58] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][58] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[14][58] = YELLOW + "0 "
    board[19][60] = "  "
    board[19][59] = '  '

    board[18][64] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][64] = YELLOW + "0 "
    board[18][63] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][63] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][63] = YELLOW + "0 "
    board[18][62] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][62] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][62] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][62] = YELLOW + "0 "
    board[18][61] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][61] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][61] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][61] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[14][61] = YELLOW + "0 "

    board[15][75] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[14][75] = YELLOW + "0 "
    board[15][71] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[14][71] = YELLOW + "0 "
    board[15][73] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[14][73] = YELLOW + "0 "
    board[11][74] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[10][74] = YELLOW + "0 "
    board[11][72] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[10][72] = YELLOW + "0 "

    board[19][82] = '  '
    board[19][80] = '  '
    board[19][81] = '  '

    board[15][87] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][92] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][93] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][88] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][89] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][90] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][91] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][94] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[9][89] = YELLOW + "0 "
    board[9][90] = YELLOW + "0 "
    board[9][91] = YELLOW + "0 "
    board[9][92] = YELLOW + "0 "

    board[19][92] = '  '
    board[19][91] = '  '
    board[19][89] = '  '
    board[19][90] = '  '
    board[19][93] = '  '

    board[18][97] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][98] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][98] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][99] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][99] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][99] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][100] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][100] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][100] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][100] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][107] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][106] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][106] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][105] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][105] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][105] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][104] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][104] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][104] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][104] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'

    board[15][110] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][111] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][112] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][113] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][114] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][115] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[13][110] = YELLOW + "0 "
    board[13][111] = YELLOW + "0 "
    board[13][112] = YELLOW + "0 "
    board[13][113] = YELLOW + "0 "
    board[13][114] = YELLOW + "0 "
    board[13][115] = YELLOW + "0 "

    board[18][120] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][121] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][121] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][122] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][122] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][122] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][123] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][123] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][123] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][123] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][124] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][124] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][124] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][124] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[14][124] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][125] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][125] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][125] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][125] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[14][125] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[13][125] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][126] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][126] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][126] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][126] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[14][126] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[13][126] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[12][126] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][127] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][127] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][127] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][127] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[14][127] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[13][127] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[12][127] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][127] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][128] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][128] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][128] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][128] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[14][128] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[13][128] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[12][128] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][128] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[10][128] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[18][129] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[17][129] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[16][129] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[15][129] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[14][129] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[13][129] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[12][129] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[11][129] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[10][129] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'
    board[9][129] = '\x1b[0;30;' + col[M.level] + RED + "__" + '\x1b[0m'

    board[18][138] = GRE + " |"
    board[17][138] = GRE + " |"
    board[16][138] = GRE + " |"
    board[15][138] = GRE + " |"
    board[14][138] = GRE + " |"
    board[13][138] = GRE + " |"
    board[12][138] = GRE + " |"
    board[11][138] = GRE + " |"
    board[10][138] = GRE + " |"
    board[9][138] = GRE + " |"
    board[8][138] = GRE + "-|"
    board[7][138] = GRE + " |"
    board[6][138] = GRE + "-|"
    board[6][137] = GRE + "--"
    board[6][136] = GRE + "--"
    board[6][135] = GRE + "|-"
    board[7][135] = GRE + "| "
    board[8][135] = GRE + "|-"
    board[8][136] = GRE + "--"
    board[8][137] = GRE + "--"

    ene.clear()
    ene.append(enemy(18, 16))
    ene.append(enemy(18, 18))
    ene.append(enemy(18, 25))
    ene.append(enemy(18, 28))
    ene.append(enemy(18, 35))
    ene.append(enemy(18, 45))
    ene.append(enemy(18, 48))

    ene.append(enemy(18, 73))
    ene.append(enemy(18, 75))
    ene.append(enemy(18, 83))
    ene.append(enemy(18, 102))
    ene.append(enemy(18, 115))
    ene.append(enemy(18, 112))

    for i in ene:
        board[i.x][i.y] = alien[M.level]
