def main():
    total_count = int(input())
    calculate_days(total_count)

def calculate_days(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 2 + 2
    print(count)
main()


