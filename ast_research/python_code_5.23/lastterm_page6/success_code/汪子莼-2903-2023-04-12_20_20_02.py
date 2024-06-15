def main():
    num = eval(input())
    calculate_e(num)
import math
def calculate_e(num):
    lst=[1]
    for i in range(1,num+1):
        b=1/(math.factorial(i))
        lst.append(b)
    print("%.6f"%sum(lst))
main()


