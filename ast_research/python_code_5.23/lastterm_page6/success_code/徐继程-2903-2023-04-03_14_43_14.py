def main():
    num = eval(input())
    calculate_e(num)
def jiecheng(m):
    sum=0
    while m!=0:
        sum*=m
        m-=1
def calculate_e(num):
    sum=1
    for i in range(num):
        sum+=1/jiecheng(i)
    print(sum)
main()


