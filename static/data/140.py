def main():
    a = int(input())
    calculate_sum(a)

def calculate_sum(a):
    total_sum = 0
    current_value = 0
    
    for x in range(a):
        current_value = current_value * 10 + a
        total_sum += current_value
    
    print(total_sum)

main()
#使用 Python 的大整数处理功能，例如使用 int 类型来直接进行大整数运算，而不是将大整数转换为字符串。