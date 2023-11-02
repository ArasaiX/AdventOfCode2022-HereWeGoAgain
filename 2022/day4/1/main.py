

def main():
    file = open("../input.txt", "r")
    total = 0
    for line in file:
        first_number = int(line[0:line.index("-")])
        second_number = int(line[(line.index("-")+1):line.index(",")])
        third_number = int(line[(line.index(",")+1):line.index("-", int(line.index(",")))])
        fourth_number = int(line[(line.index("-", int(line.index(","))))+1:-1])
        if ((first_number >= third_number) and (second_number <= fourth_number)) or ((third_number >= first_number) and (fourth_number <= second_number)):
            total = total + 1
    print("El total es:",total)


main()


