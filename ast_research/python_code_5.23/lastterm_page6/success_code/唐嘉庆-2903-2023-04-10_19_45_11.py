def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    a=1
    b=1
    for i in range(1,x+1):
       a=a*(1/i)
       b+=a
    print('%.6f'%(b))
main()


