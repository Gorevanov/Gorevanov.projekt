field = [7, 8, 9,
        4, 5, 6,
        1, 2, 3]

victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

def print_field():
    print(field[0], end="|")
    print(field[1], end="|")
    print(field[2])

    print(field[3], end="|")
    print(field[4], end="|")
    print(field[5])

    print(field[6], end="|")
    print(field[7], end="|")
    print(field[8])

def step_field(step,symbol):
    ind = field.index(step)
    field[ind] = symbol

def get_result():
    win = ""

    for i in victories:
        if field[i[0]] == "x" and field[i[1]] == "x" and field[i[2]] == "x":
            win = "X"
        if field[i[0]] == "o" and field[i[1]] == "o" and field[i[2]] == "o":
            win = "O"

    return win


game_over = False
player = True

while game_over == False:
    print_field()

    if player == True:
        symbol = "x"
        step = int(input("Ход игрока Х: "))
    else:
        symbol = "o"
        step = int(input("Ход игрока О: "))

    step_field(step, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

    player = not (player)

print_field()
print("Победил", win)