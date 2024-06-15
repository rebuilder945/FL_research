def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
    s=1
    t=1
    for x in range(1,a+1):
        t=t*x
        s=s+(1/t)
    print('%.6f'%s)
main()


