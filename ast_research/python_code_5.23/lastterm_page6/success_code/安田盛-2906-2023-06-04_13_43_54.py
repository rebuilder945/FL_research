def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(n):
    a=0
    while n>0:
        a+=1
        n=n-n//2-2
    print(a)

main()


