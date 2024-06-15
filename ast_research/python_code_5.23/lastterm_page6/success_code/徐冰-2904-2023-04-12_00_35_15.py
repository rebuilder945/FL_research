def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    n=a
    b=str(a)
    sum=0
    while n>0:
        sum=sum+int(n*b)
        n=n-1
    print(sum)
main()

