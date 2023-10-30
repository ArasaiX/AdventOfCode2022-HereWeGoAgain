
#  Win: 6   Draw: 3    Lose: 0

#  Rock: 1  Paper: 2  Scissors 3

# Rock: A / X

# Paper: B / Y

# Scissors: C / Z

# X Perder  Y Empate Z Ganar


def main():
    file = open("../input.txt", "r")
    total = 0
    for line in file:
        suma = 0
        suma = calculate_points(line)
        if (type(suma) != False):
            total = total + int(suma)
        else:
            print(line)
    print("The total score are: " ,total)

def calculate_points(play):
    print("LINE!", play, end="")
    if (play[0] == "A"):
        if (play[-2] == "X"):
            print(f'Playing A ({play[0]}) VS X ({play[-2]}) the result are 3 ')
            return 3
        elif (play[-2] == "Y"):
            print(f'Playing A ({play[0]}) VS Y ({play[-2]}) the result are 4 ')
            return 4
        elif (play[-2] == "Z"):
            print(f'Playing A ({play[0]}) VS Z ({play[-2]}) the result are 8 ')
            return 8
    elif (play[0] == "B"):
        if (play[-2] == "X"):
            print(f'Playing B ({play[0]}) VS X ({play[-2]}) the result are 1 ')
            return 1
        elif (play[-2] == "Y"):
            print(f'Playing B ({play[0]}) VS Y ({play[-2]}) the result are 5 ')
            return 5
        elif (play[-2] == "Z"):
            print(f'Playing B ({play[0]}) VS Z ({play[-2]}) the result are 9 ')
            return 9
    elif (play[0] == "C"):
        if (play[-2] == "X"):
            print(f'Playing C ({play[0]}) VS X ({play[-2]}) the result are 2 ')
            return 2
        elif (play[-2] == "Y"):
            print(f'Playing C ({play[0]}) VS Y ({play[-2]}) the result are 6 ')
            return 6
        elif (play[-2] == "Z"):
            print(f'Playing C ({play[0]}) VS Z ({play[-2]}) the result are 4 ')
            return 7
    else:
        return 0





main()

