def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    e = 1
    factor = 1
    for i in range(1, n+1):
        factor *= i         # 计算当前的阶乘
        e += 1 / factor     # 累加 1/factor
    print('%.6f' % e)       # 输出结果，保留小数点后六位有效数字
main()


