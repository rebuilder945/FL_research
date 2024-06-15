def main():
    num = eval(input())
    calculate_e(num)
def jiecheng(m):
    sum=1
    while m!=0:
        sum*=m
        m-=1
    return sum
def calculate_e(num):
    sum=1
    for i in range(num):
        sum+=1/jiecheng(i)
    print('%.6f'%(sum-1))
main()


