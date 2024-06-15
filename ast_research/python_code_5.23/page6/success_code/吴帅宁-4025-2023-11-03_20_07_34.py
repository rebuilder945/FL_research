def main():
    num = eval(input())
    calculate_e(num)
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
def calculate_e(num):
    lst=[]
    for i in range(num):
        b=float(1/factorial(num))
        lst.append(b)
    print("%.6f"%(sum(lst)))
main()


