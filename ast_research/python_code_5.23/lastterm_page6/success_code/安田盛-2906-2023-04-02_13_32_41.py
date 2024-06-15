def main():
    total_count = int(input())
    calculate_days(total_count)
    print(calculate_days(total_count))
def calculate_days(total_count):
    s=total_count
    for i in range(1,total_count+1):
        N=s
        s=N-2-int(N/2)
        

        if s<=0:
            return i

main()


