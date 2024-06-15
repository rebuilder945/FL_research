def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        sum=0
        f="1"
        for i in range(0,a):
            sum=sum+a*int(f*(i+1))
        print(sum)
main()

