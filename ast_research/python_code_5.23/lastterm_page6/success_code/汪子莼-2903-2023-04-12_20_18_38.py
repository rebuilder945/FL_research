def main():
    num = eval(input())
    calculate_e(num)
import math
def calculate_e(num):
    lst=[]
    for i in range(num):
        b=1/(math.factorial(i))
        lst.append(b)
    print("%.6f"%sum(lst))
main()


