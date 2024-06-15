def main():
    num = eval(input())
    calculate_e(num)
import math
def calculate_e(x):
    sum=0
    for y in range(x+1):
        m=math.factorial(y)
        sum+=1/m
    print("%.6f"%sum)

main()


