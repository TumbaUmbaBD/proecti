def risowat_doska(doska):
    for line in doska:
        print(" | ".join(line))
        print("-" * 9)
def check_winner(doska):
    for i in range(3):
        if doska[i][0] == doska[i][1] == doska[i][2] != " ":
            return doska[i][0]
        if doska[0][i] == doska[1][i] == doska[2][i] != " ":
            return doska[0][i]
    if doska[0][0] == doska[1][1] == doska[2][2] != " ":
        return doska[0][0]
    if doska[0][2] == doska[1][1] == doska[2][0] != " ":
        return doska[0][2]
    return None
def hod():
    doska = [[" " for _ in range(3)] for _ in range(3)]
    chei_hod = "X"
    for _ in range(9):
        risowat_doska(doska)
        line = int(input(f"Player {chei_hod}, see the line number (0, 1, 2): "))
        col = int(input(f"зlayer {chei_hod}, enter the column number (0, 1, 2): "))
        if doska[line][col] == " ":
            doska[line][col] = chei_hod
            winner = check_winner(doska)
            if winner:
                risowat_doska(doska)
                print(f"{winner} has won the game!")
                return
            chei_hod = "O" if chei_hod == "X" else "X"
        else:
            print("occupied.")
    risowat_doska(doska)
    print("DRAW,there is no winner")
hod()