def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    list0=[1]
    for i in range(num):
        b=1
        for s in range(i+1):
            b=b/(s+1)
        list0.append(b)
    print('%.6f'%sum(list0))
main()


