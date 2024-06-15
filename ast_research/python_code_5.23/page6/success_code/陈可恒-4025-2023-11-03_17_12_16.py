def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(n):
        e = 1
        for i in range(1,1+n):
            for x in range(1,i):
                   i = i*x
            e = e +1/i
        print('%.6f'%e)
main()


