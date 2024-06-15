def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    import math
    s=[1/math.factorial(i) for  i in range(0,n+1)]
    a=sum(s)
    print("%.6f"%(a))  

main()


