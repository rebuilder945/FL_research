def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    import math
    s=[1/math.factorial(i) for i in range(n+1)]
    print("%.6f"%(sum(s)))   
main()


