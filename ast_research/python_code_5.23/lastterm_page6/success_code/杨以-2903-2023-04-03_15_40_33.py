def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    import math
    e=0
    for num in range(0,num+1):
        e=e+1/(factorial(num))
    print("%.6f"%e)
main()


