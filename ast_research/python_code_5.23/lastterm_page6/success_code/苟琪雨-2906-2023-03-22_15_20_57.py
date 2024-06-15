def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    n=1
    while total_count>int(total_count/2)+2:
        total_count=int(total_count/2)-2
        n=n+1
    else:
        n=n+1
    print(n)
main()


