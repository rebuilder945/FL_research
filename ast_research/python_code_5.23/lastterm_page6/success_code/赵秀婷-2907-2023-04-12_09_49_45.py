def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    a = calculate_capital(N, M)
    print("%.4f" % a)

def calculate_capital(N, M):
    return N * (1 + 0.003) ** M

main()



