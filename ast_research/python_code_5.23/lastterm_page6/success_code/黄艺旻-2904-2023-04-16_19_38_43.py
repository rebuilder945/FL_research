def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sum=0
    tmp=a
    for i in range(1,a+1):
        sum=sum+a
        a=int(str(tmp)*(i))
    print(sum)
main()

