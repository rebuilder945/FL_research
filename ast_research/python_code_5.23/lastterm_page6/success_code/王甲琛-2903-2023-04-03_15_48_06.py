def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    list0=[1]
    b=1
    for i in range(num):
        for x in range(i):
            b=b/(x+1)
    list0.append(b)       
    print(sum(list0))
main()


