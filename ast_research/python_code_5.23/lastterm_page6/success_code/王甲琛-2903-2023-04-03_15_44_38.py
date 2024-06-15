def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    list0=[]
    a=1
    b=1
    for i in range(num):
        for x in range(i):
            b=b/(x+1)
        a=a+b
        list0.append(a)
    print(sum(list0))
main()


