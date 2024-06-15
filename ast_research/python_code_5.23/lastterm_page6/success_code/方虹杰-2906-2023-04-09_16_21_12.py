def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    n=total_count
    m=0
    while n>0:
        m=m+1
        n=n//2-2
    print(m)
                
                
main()


