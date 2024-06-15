def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    day = 1
    remaining = total_count
    while remaining > 0:
        remaining = (remaining // 2) - 2
        if remaining > 0:
            day += 1
    print(day)
main()


