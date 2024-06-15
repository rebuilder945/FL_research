def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    lst=[1]
    b=1
    for x in range(num-1):
        b=b*(x+1)
        a=1/b
        lst.append(a)
    c=sum(lst)
    print("%.6f"%(c))
main()


