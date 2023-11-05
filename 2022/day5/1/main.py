#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

stack = [
    [],
    ["N", "Z"],
    ["D", "C", "M"],
    ["P"]
]

def main():
    file = open("../input.txt", "r")
    for line in file:
        print(line)
        line = line.replace(" ", "")
        move = 0
        start_position = 0
        end_position = 0
        aux = 0
        move = int(line[line.index("e")+1:line.index("f")])
        start_position = int(line[line.index("om")+2:line.index("t")])
        end_position = int(line[line.index("to")+2:])
        
        for x in range(move):
            print(x)
            print(stack[end_position])
            stack[end_position].append(stack[start_position][x])
            stack[start_position].pop
    print(stack)



main()