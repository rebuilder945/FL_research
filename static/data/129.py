def main():
    total_count = int(input())
    calculate_days(total_count)

def calculate_days(total_count):
    d = 0
    h = total_count
    for i in range(total_count):  
        # 提供一个参数来指定迭代的次数
        # range() 函数需要指定一个起始值、结束值以及可选的步长
        if i > 1/2 * h + 2:
            d = d + 1
        else:
            break
    print(d)

main()