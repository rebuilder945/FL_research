def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(num):
    day = 0
    while num > 0:
        num = num - num // 2 - 1
        day = day + 1
    print(day)
main()


