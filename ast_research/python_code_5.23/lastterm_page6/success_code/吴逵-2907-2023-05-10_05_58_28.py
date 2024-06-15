def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    r = 0.003  # 年利率
    for i in range(M):
        N = N * (1 + r)  # 计算新的本金
    print("%.4f" % N)  # 输出结果，保留小数点后四位

def main():
    N, M = map(int, input().split())
    calculate_capital(N, M)
main()



