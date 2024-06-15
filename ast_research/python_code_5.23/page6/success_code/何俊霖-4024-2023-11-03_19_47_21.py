def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        sum=0
        a=str(a)
        for i in range(1,int(a)+1):
            sum=sum+int(a*i)
        print(sum)
main()

