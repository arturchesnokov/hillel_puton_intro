S = '#'

game = [
    [S, S, S],
    [S, S, S],
    [S, S, S],
]


# Печатаем игровое поле
def print_game():
    print(" ", 1, 2, 3)
    print(1, game[0][0], game[0][1], game[0][2])
    print(2, game[1][0], game[1][1], game[1][2])
    print(3, game[2][0], game[2][1], game[2][2])


# заполнение игрового поля по указаным координатам в зависимости от текущего игрока
def set_value(x, y):
    game[x][y] = "x" if first_player else "o"


# проверка игровых линий
def winner():
    if (game[0][0] == game[0][1] == game[0][2] != S
            or game[1][0] == game[1][1] == game[1][2] != S
            or game[2][0] == game[2][1] == game[2][2] != S
            or game[0][0] == game[1][0] == game[2][0] != S
            or game[0][1] == game[1][1] == game[2][1] != S
            or game[0][2] == game[1][2] == game[2][2] != S
            or game[0][0] == game[1][1] == game[2][2] != S
            or game[2][0] == game[1][1] == game[0][2] != S):
        return True
    else:
        return False


# проверка координат
def not_used(x, y):
    return game[x][y] == S


# проверка введенных данных
def input_check(string):
    try:
        s = [int(num) for num in string.split(",")]
    except ValueError:
        print("Please input coordinates in correct format")
        return None

    if len(s) == 2 and 1 <= s[0] <= 3 and 1 <= s[1] <= 3:
        s[0] -= 1
        s[1] -= 1
        return s
    else:
        print("Wrong coordinates")
        return None


first_player = True

print("Please input coordinates in format 'x,y' and use number 1-3")
print_game()
while True:
    coordinates = input_check(input())
    if coordinates is None:
        continue
    else:
        x, y = coordinates

    if not_used(x, y):
        set_value(x, y)
    else:
        print("This position already used! Try again")
        continue

    if winner():  # проверяем поле
        print("First player wins") if first_player else print("Second player wins")
        print_game()
        break
    first_player = False if first_player else True  # меняем игрока
    print_game()
