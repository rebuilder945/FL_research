def main():
    total_count = int(input())
    calculate_days(total_count)
from math import *
def calculate_days(w):
    days = 0  # 计数器，记录卖出的天数

    while w> 0:
        days += 1
        if w == 1:  # 若只剩下一个西瓜，则直接卖出并结束循环
            break
        w= (w// 2) + 2

    print(days)
        
main()


