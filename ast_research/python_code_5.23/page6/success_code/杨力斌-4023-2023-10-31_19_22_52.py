def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    days = 0
    while total_count > 0:
        total_count = total_count - total_count/2 - 2
        days = days + 1
main()


