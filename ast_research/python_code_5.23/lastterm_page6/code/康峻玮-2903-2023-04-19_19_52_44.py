def main():
    num = eval(input())
    calculate_e(num)
import math
def  calculate_e(num):
    i=1
    a=1
    while i<num+1:
        a+=1/float((math.factorial(i)）
        i=i+1
    print("%.6f" % (a))
main()


