def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    y=1
    if num==1:
        print('%.6f'%(e))
    else:
        for x in range(num):
            for i in range(1,x):
                y=y*(i+1)
            e=e+1/y
        print('%.6f'%(e))
main()


