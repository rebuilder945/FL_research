def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(n):
    count = 0  # 记录已经卖出的瓜数
    day = 0  # 记录天数

    while count < n:
        day += 1  # 天数加一
        if day == 1:
            # 第一天卖出（n/2）+2个瓜
            count += n // 2 + 2
        else:
            # 其他天卖出上一天剩余瓜数的一半再加2
            count += (count // 2) + 2

    print(day)  # 输出天数
main()


