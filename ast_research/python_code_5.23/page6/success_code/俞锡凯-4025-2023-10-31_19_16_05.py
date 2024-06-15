def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    for i in range(1,num+1):
        for m in range(1,i+1):
            cj=i*m
            e=1+1/cj
    print('%.6f'%e)
main()


