def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(n):
    m=0
    while True:
        if n<=0:
            break
        else:
            if n%2!=0:
                n=n-(n-1)/2-2
            else:
                n=n/2-2
            m=m+1
    print(m)
main()


