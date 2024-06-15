def main():
    num = eval(input())
    calculate_e(num)
import sys
sys.setrecursionlimit(10000)
def p(i):
    if i == 0:
        return 1
    else:
        return i * p(i-1)def calculate_e(num):
    i = 0
    sume=1
    while i < num:
        i = i + 1
        sume += (1/p(i))
    print("%.6f" % (sume))
main()


