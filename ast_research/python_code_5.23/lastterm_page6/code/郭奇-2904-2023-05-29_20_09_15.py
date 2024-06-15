def main():
    a=int(input())
    calculate_sum(a)
     def calculate_sum(a):
    # 初始化变量
    total = 0
    num = a

    # 循环计算每一项的值并累加到总和中
    for i in range(a):
        total += num
        num = num * 10 + a
    return num
return calculate_sum(a)
main()

