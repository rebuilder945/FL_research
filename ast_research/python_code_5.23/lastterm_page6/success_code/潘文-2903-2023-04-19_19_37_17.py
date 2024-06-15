def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
        b=1
        for i in range(1,a+1):
                c=1
                for j in range(1,i+1):
                        c*=j
                b+=1/c
        print('%.6f'%b)
main()


