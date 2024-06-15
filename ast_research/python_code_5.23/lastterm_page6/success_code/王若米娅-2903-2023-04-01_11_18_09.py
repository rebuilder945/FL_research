def main():
    num = eval(input())
    calculate_e(num)

    return calculate_e(num)
def factorial(x):
    if x==0:
        return 1
    else:
        return x* factorial(x-1)
def calculate_e(num):
    lst=[]
    for i in range(num):
        c=1/factorial(i)
        lst.append(c)
    return "%.6f"%(sum(lst))
main()


