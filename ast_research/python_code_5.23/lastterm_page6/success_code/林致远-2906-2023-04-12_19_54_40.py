def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    days = 1
    total_count = total_count/2 - 2
    while total_count >= 4:
        total_count = total_count/2 -2
        days = days + 1
    days = days + 1
    print(days)
main()


