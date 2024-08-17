"""A tictactoe game
"""
import numpy as np
a1 = "_"
a2 = "_"
a3 = "_"
a4 = "_"
a5 = "_"
a6 = "_"
a7 = "_"
a8 = "_"
a9 = "_"
table = np.array([[a1, a2, a3],
                  [a4, a5, a6],
                  [a7, a8, a9]])

class Wrongposition(Exception):
    pass
class Positionalreadyfilled(Exception):
    pass

def playerx(firstplayer):
    if firstplayer == "a1":
        if (table[0][0] == 'X' or table[0][0] == 'Y') and firstplayer == "a1":
            raise Positionalreadyfilled('this spot has been taken')
        table[0][0] = 'X'
        print(table)
    elif firstplayer == "a2":
        if (table[0][1] == 'X' or table[0][1] == 'Y') and firstplayer == "a2":
            raise Positionalreadyfilled('this spot has been taken')
        table[0][1] = 'X'
        print(table)
    elif firstplayer == "a3":
        if (table[0][2] == 'X' or table[0][2] == 'Y') and firstplayer == "a3":
            raise Positionalreadyfilled('this spot has been taken')
        table[0][2] = 'X'
        print(table)
    elif firstplayer == "a4":
        if (table[1][0] == 'X' or table[1][0] == 'Y') and firstplayer == "a4":
            raise Positionalreadyfilled('this spot has been taken')
        table[1][0] = 'X'
        print(table)
    elif firstplayer == "a5":
        if (table[1][1] == 'X' or table[1][1] == 'Y') and firstplayer == "a5":
            raise Positionalreadyfilled('this spot has been taken')
        table[1][1] = 'X'
        print(table)
    elif firstplayer == "a6":
        if (table[1][2] == 'X' or table[1][2] == 'Y') and firstplayer == "a6":
            raise Positionalreadyfilled('this spot has been taken')
        table[1][2] = 'X'
        print(table)
    elif firstplayer == "a7":
        if (table[2][0] == 'X' or table[2][0] == 'Y') and firstplayer == "a7":
            raise Positionalreadyfilled('this spot has been taken')
        table[2][0] = 'X'
        print(table)
    elif firstplayer == "a8":
        if (table[2][1] == 'X' or table[2][1] == 'Y') and firstplayer == "a8":
            raise Positionalreadyfilled('this spot has been taken')
        table[2][1] = 'X'
        print(table)
    elif firstplayer == "a9":
        if (table[2][2] == 'X' or table[2][2] == 'Y') and firstplayer == "a9":
            raise Positionalreadyfilled('this spot has been taken')
        table[2][2] = 'X'
        print(table)
    else:
        raise Wrongposition('enter a valid position')
def playero(firstplayer):
    if firstplayer == "a1":
        if (table[0][0] == 'X' or table[0][0] == 'Y') and firstplayer == "a1":
            raise Positionalreadyfilled('this spot has been taken')
        table[0][0] = 'O'
        print(table)
    elif firstplayer == "a2":
        if (table[0][1] == 'X' or table[0][1] == 'Y') and firstplayer == "a2":
            raise Positionalreadyfilled('this spot has been taken')
        table[0][1] = 'O'
        print(table)
    elif firstplayer == "a3":
        if (table[0][2] == 'X' or table[0][2] == 'Y') and firstplayer == "a3":
            raise Positionalreadyfilled('this spot has been taken')
        table[0][2] = 'O'
        print(table)
    elif firstplayer == "a4":
        if (table[1][0] == 'X' or table[1][0] == 'Y') and firstplayer == "a4":
            raise Positionalreadyfilled('this spot has been taken')
        table[1][0] = 'O'
        print(table)
    elif firstplayer == "a5":
        if (table[1][1] == 'X' or table[1][1] == 'Y') and firstplayer == "a5":
            raise Positionalreadyfilled('this spot has been taken')
        table[1][1] = 'O'
        print(table)
    elif firstplayer == "a6":
        if (table[1][2] == 'X' or table[1][2] == 'Y') and firstplayer == "a6":
            raise Positionalreadyfilled('this spot has been taken')
        table[1][2] = 'O'
        print(table)
    elif firstplayer == "a7":
        if (table[2][0] == 'X' or table[2][0] == 'Y') and firstplayer == "a7":
            raise Positionalreadyfilled('this spot has been taken')
        table[2][0] = 'O'
        print(table)
    elif firstplayer == "a8":
        if (table[2][1] == 'X' or table[2][1] == 'Y') and firstplayer == "a8":
            raise Positionalreadyfilled('this spot has been taken')
        table[2][1] = 'O'
        print(table)
    elif firstplayer == "a9":
        if (table[2][2] == 'X' or table[2][2] == 'Y') and firstplayer == "a9":
            raise Positionalreadyfilled('this spot has been taken')
        table[2][2] = 'O'
        print(table)
    else:
        raise Wrongposition('enter a valid position')
