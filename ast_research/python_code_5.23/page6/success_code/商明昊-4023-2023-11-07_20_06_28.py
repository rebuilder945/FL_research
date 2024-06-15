def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(t):
    n=0
    while True:
        if t%2==1:
            t=(t+1)/2-2
            n=n+1
        else:
            t=t/2-2
            n=n+1
        if t<0:
            n=n-1
            break 
    print(n) 
main()


