def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    x=1
    for i in range(num):
           x=x*1/(i+1)
           e=e+x
    print('%.6f'%(e))
main()


