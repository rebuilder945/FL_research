def main():
    total_count = int(input())
    calculate_days(total_count)

def calculate_days(total_count):
    a = 0
    while total_count > 0:
        total_count = total_count + 1  
        # 使用加号来增加 total_count 的值
        # 尝试将 total_count 的值更新为一个元组 (total_count,)，而不是一个整数
        a += 1
    print(a)

main()