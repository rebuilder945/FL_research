def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(n):
        b=1
        a=1
        for i in range (1,n+1):
                b=1/i*b
                a=a+b
        print ('%.6f'%a)
main()


