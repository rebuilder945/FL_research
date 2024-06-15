def main():
    num = eval(input())
    calculate_e(num)
import sys
import traceback
sys.setrecursionlimit(100000)
def factorial(n):
    if(n<=1):
        return 1
    else:
        return factorial(n-1) * n
def calculate_e(num):
    x=0
    e=1
    while x<num:
        x+=1
        a=1/factorial(x)
        e=e+a
    print("%.6f"%e)
main()


