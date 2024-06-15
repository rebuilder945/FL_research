def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    n=total_count
    i=0
    while n>0:
        i=i+1
        a=int(n/2)
        b=a+2
        n=n-b
    print(i)
main()


