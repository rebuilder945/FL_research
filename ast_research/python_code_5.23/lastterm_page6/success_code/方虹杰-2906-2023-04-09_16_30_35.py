def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    n=total_count
    m=0
    while n>0:
        if n%2==0:
             n=n//2-2
             m=m+1
        else:
             n=n-2-(n-1)*0.5
             m=m+1
    print(m)
                
                
main()


