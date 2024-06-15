def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(SB):
    i = 0
    while SB > 0:
        i += 1
        sell_count = SB // 2 + 2
        remain_count = SB - sell_count
        SB = remain_count
    print(i)
main()


