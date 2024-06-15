def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    days = 0
    while n > 0 :
        days = days + 1
        m = int(n/2)
        n = n - (m+2)
        if n <= 0:
            break
    print(days)
main()


