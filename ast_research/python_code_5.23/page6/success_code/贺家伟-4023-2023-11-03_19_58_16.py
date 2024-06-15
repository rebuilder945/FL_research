def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    n=total_count
    d=0
    if n<=4:
        d=1
    else:
        while n>0:
            n=n-int(n/2)-2
            d+=1
    print(d)
        
main()


