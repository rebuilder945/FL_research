def main():
    num = eval(input())
    calculate_e(num)
     return "%.6f"%(calculate_e(num))
def factorial(x):
    if x==0:
        return 1
    else:
        return x* factorial(x-1)
def calculate_e(x):
    lst=[]
    for i in range(x):
        c=1/factorial(i)
        lst.append(c)
    return sum(lst)
main()


