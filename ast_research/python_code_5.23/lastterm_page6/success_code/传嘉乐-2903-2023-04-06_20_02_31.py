def main():
    num = eval(input())
    calculate_e(num)
import math
def calculate_e(num):
    i=0
    e=0
    while i<num:
        i+=1
        e += 1/math.factorial(i)
    print(e)
main()
main()


