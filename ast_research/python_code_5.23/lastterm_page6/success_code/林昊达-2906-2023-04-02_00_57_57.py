def main():
    total_count = int(input())
    calculate_days(total_count)
def  calculate_days(total_count):
        days = 0
        while total_count > 0:
                total_count=round(total_count/2)-2
                days += 1
        print(days)
main()


