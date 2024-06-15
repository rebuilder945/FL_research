def main():
    num = eval(input())
    calculate_e(num)
from math import factorial
x = 2
y = 0
i = 1
while x - y > 10e-6:
    y = x
    i += 1
    x += 1/factorial(i)
print("%.6f"%x)
main()


