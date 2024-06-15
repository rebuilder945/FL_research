def main():
    num = eval(input())
    calculate_e(num)
import math
def  calculate_e(num):
    i=1
    e=1
    while i<=num:
        e+=1/float(math.factorial(i))
        i=i+1
    print("%.6" % (e))
main()


