

dct = {'a':1, 'b':2,'c':3,'d':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9,'j':10, 'k':11,'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A': 27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32,'G':33,'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, '0':41,'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}

def main():
    total = []
    result = []
    file = open("../input.txt", "r")
    aux_str = ''
    j = 1
    for line in file:
        print("J-->", j, "actual line", line)
        if (j % 3 == 0):
            print(f'J es divisible entre 3, valor de j {j}')
            print("Guardamos la string auxiliar en el array result", aux_str)
            aux_str = aux_str + line
            result.append(aux_str)
            print("RESULT", result)
            item = get_points_of_group(aux_str)
            print("ITEM", item)
            value_of_item = dct.get(item)
            total.append(value_of_item)
            aux_str = ''
            result = []
            print("elementos actuales del array", result)
        else:
            print(f'J no es divisible entre 3, valor de j{j}')
            aux_str = aux_str + line
            print(f'Sumamos la aux string a la line actual {aux_str}')
        j = j + 1
    print("RESULTADO FINAL!", sum(total))

    

def get_points_of_group(result):
    print("2",result)
    item = ''
    str_sliced = result.split("\n")
    str_sliced.pop(3)
    print("SLICED", str_sliced)
    for char in str_sliced[0]:
        for char2 in str_sliced[1]:
            if (char == char2):
                print("EO", char)
                for char3 in str_sliced[2]:
                    if (char == char3):
                        print("CHAR", char)
                        item = char

                        return item
    
        # for line in file:
    #     item = ''
    #     # print(file.read)
    #     half_line = len(line) / 2
    #     first_half_str = line[0:int(half_line)]
    #     second_half_str = line[int(half_line):-1]
    #     for char in first_half_str:
    #         if (item != ""):
    #             break
    #         for char2 in second_half_str:
    #             if (char == char2):
    #                 item = char
    #                 print(item)
    #                 break
    #     value_of_item = dct.get(item)
    #     result.append(value_of_item)
    #     print(value_of_item)
    # print("RESULT", sum(result))

main()