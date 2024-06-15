def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    days = 0
    while total_count > 0:
        days += 1
        if days == 1:
            total_count = (total_count // 2) + 2
        else:
            total_count = (total_count // 2) + 2
    print(days)
main()


