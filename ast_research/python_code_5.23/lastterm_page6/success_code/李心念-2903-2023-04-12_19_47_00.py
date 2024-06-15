def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    b = [1]
    for i in range(n):
        a = 1
        for x in range(i+1):
            a = a*(x+1)
        b.append(1/a)
    print('%.6f'%(sum(b)))
main()


