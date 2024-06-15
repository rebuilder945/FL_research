def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(n):
    m=0
    while n>0:
        n=n/2-2
        m+=1
    print(m)
main()


