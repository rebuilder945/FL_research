def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    sum=1
    fac=1
    for i in range(num):
        fac *= (i+1)
        sum+=1/fac
    print('{:.6f}'.format(sum))
main()


