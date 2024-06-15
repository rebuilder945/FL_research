def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(N):
    i=0
    while N>0:
        i+=1
        N=N/2-2
    print(i)
main()


