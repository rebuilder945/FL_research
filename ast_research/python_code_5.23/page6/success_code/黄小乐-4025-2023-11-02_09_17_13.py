def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    s=1
    num=1
    for i in range (1,n+1):
        s=s*i
        num=num+1/s
    print('%.6f' % num)
main()


