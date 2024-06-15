def main():
    num = eval(input())
    calculate_e(num)
import math
def calculate_e(num):
    e=1
    for x in range(num):
        x += 1
        x = math.factorial(x)
        e += 1/x
    print('%.6f' % e)
main()


