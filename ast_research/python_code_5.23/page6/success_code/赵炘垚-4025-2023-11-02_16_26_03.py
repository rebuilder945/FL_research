def main():
    num = eval(input())
    calculate_e(num)

def calculate_e(num):
    print(f"{1+sum(1/fac(i) for i in range(1,num+1)):.6f}")

from functools import reduce
from operator import mul

def fac(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

main()


