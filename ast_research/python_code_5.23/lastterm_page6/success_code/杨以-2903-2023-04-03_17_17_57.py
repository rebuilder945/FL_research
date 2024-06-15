def main():
    num = eval(input())
    calculate_e(num)
import math

def calculate_e(n):
    e = 1
    factorial = 1

    for i in range(1, n+1):
        factorial *= i
        e += 1/factorial
main()


