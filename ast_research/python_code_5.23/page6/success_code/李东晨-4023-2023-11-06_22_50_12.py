def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(N):
    a=0
    while N>0:
        a+=1
        N=N-int(N/2)-2
    print(a)
main()


