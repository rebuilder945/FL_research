def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num):
    a = 1
    b = 1
    c = 1
    for i in range(num):
        c = c*(1/a)
        b = b+c
        a = a+1
    print('%.6f'%b)
main()


