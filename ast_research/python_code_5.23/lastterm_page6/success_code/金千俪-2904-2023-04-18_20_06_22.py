def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    sum=0
    t=0
    tt=len(str(a))
    for i in range(a):
        t=a+t*(10**tt)
        sum=sum+t
    print(sum)
main()

