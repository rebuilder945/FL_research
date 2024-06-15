def main():
    num = eval(input())
    calculate_e(num)
import math
n = int(input("请输入正整数n："))
e = 0
for i in range(n):
    e += 1 / math.factorial(i)
print("{:.2f}".format(e))

main()


