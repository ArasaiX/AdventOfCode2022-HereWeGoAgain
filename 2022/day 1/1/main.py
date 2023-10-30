result = []

def main():
    file = open("input.txt", "r")
    auxiliar_sum_results = 0
    for line in file:
        if (line != "\n"):
            result.append(int(line))
        else:
            if (auxiliar_sum_results < sum(result)):
               auxiliar_sum_results = sum(result)
            result.clear()
    print("The maximum amount of Calories are... \n\n *********--->  ", auxiliar_sum_results, "  <---*********")
            
main()