result = []
totals = []

def main():
    file = open("input.txt", "r")
    auxiliar_sum_results = 0
    for line in file:
        if (line != "\n"):
            result.append(int(line))
        else:
            totals.append(sum(result))
            if (auxiliar_sum_results < sum(result)):
               auxiliar_sum_results = sum(result)
            result.clear()
    totals.sort(reverse=True)
    print("The maximum amount of Calories of the three first elvees are... \n\n *********--->  ", totals[0] + totals[1] + totals[2], "  <---*********")
            
main()