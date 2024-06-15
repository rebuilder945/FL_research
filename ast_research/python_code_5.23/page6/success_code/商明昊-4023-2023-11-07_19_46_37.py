def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(t):
    n=0
    for i in range(t):
        if t%2==1:
            t=(t-1)/2-2
            n=n+1
            if t<0:
                break 
        else:
            t=t/2-2
            n=n+1
            if t<0:
                break 
    print(n)  
main()


