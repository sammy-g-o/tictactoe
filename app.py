from tictactoe import table, playero, playerx, Wrongposition, Positionalreadyfilled

print(table)

while True:
    while True:
        try:
            playerx(input("X's turn"))
            break
        except (Wrongposition,Positionalreadyfilled) as error:
            print(error)
    if  table[0][1] == 'X' and table[1][1] == 'X' and table[2][1] == 'X' or table[0][0] == 'X' and table[1][1] == 'X' and table[2][2] == 'X' or table[0][0] == 'X' and table[1][0] == 'X' and table[2][0] == 'X'or table[0][0] == 'X' and table[0][1] == 'X' and table[0][2] == 'X'or table[1][0] == 'X' and table[1][1] == 'X' and table[1][2] == 'X'or table[2][0] == 'X' and table[2][1] == 'X' and table[2][2] == 'X'or table[0][2] == 'X' and table[1][1] == 'X' and table[2][0] == 'X':
        print('X wins')
        break
    while True:
        try:
            playero(input("O's turn"))
            break
        except (Wrongposition,Positionalreadyfilled) as error:
            print(error)
    if  table[0][1] == 'O' and table[1][1] == 'O' and table[2][1] == 'O' or table[2][0] == 'O' and table[2][1] == 'O' and table[2][2] == 'O' or table[1][0] == 'O' and table[1][1] == 'O' and table[1][2] == 'O' or table[0][0] == 'O' and table[0][1] == 'O' and table[0][2] == 'O' or table[0][0] == 'O' and table[1][0] == 'O' and table[2][0] == 'O' or table[0][0] == 'O' and table[1][1] == 'O' and table[2][2] == 'O':
        print('O wins')
        break

print(table)
