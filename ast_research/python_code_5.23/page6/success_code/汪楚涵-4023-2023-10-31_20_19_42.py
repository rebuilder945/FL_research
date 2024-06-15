def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(total_count):
    left=total_count/2-2
    days=(left-2)/2+1
    print("%.0f"%days)
main()


