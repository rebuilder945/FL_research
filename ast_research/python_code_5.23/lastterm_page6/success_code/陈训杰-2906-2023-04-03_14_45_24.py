def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    N=total_count
    a=0
    while N>0:
        N=N/2-2
        a+=1
    print(a)
main()


