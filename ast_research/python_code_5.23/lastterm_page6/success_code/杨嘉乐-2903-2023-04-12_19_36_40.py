def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    sum=1
    m=1
    for i in range(num):
        m=m*(i+1)
        sum+=1/m
    print('%.4f'%sum)
main()


