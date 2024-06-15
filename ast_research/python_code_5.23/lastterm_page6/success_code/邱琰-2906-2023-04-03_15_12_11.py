def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(N):
    days=0
    while(N>0):
            N=N-N//2-2
            days+=1
    print(days)
main()


