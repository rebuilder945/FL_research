def main():
    num = eval(input())
    calculate_e(num)
import math
def  calculate_e(num):
    e = 0
    for i in range(num):
       e += 1 / math.factorial(i)
    print("{:.2f}".format(e))

main()


