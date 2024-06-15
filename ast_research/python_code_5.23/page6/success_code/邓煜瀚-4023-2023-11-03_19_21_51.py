def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(n):
    count=0
    while n>0:
        n=n-(n/2)-2
        count+=1
    print(count)
main()


