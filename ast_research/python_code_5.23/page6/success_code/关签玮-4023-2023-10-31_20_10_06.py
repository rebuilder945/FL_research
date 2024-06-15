def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    b=total_count
    n=0
    for i in range(total_count):
        if b>0:
            a=int(b/2)
            b=b-(a+2)
            n=n+1
        elif 0>=b:
            break
    print(n)
main()


