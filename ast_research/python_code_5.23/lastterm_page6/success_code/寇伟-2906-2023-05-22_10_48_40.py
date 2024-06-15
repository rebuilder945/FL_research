def main():
    total_count = int(input())
    calculate_days(total_count)
import math
def calculate_days(n, days=0):
    if n == 1:  # 若只剩下一个西瓜，则直接卖出并返回天数
        return days
    else:
        sell_num = math.ceil(n / 2) + 1  # 当天需要卖出的数量（向上取整）
        print(calculate_days(sell_num))
main()


