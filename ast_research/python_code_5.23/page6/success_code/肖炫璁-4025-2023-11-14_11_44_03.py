def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    num,t=1,1
    for i in range(1,n+1):
        t=t/i
        num+=t
    print('%.6f'%num)
main()


