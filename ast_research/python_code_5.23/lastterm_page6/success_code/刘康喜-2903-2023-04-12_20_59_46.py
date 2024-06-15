def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
    a=a+1
    c=1
    if a==1:
        c=1
    else:
        for i in range(2,a+1):

            b=1
            for j in range(0,i-2):
                b=b*(j+2)

                if j==i-3:
                    b=1/b
            c=c+b
    print('%.6f'%c)

main()


