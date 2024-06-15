def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    total_count=N
    days=0
    while N>3:
        if N%2==0:
            N=N-(N/2+2)
            days=days+1
        else:
            N=N-((N-1)/2+2)
            days=days+1
        if N<=3:
            break
    days=days+1
    print(days)
main()


