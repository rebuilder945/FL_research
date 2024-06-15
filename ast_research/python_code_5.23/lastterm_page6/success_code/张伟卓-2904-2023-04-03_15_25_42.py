def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        num=a
        sum=a
        for i in range(2,a+1):
                num=num*10+a
                sum+=num

        print(sum)
main()

