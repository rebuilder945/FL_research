def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    def calculate_capital(N,M):
        capital = (N*(1.003))**M
        return capital
    print(calculate_capital(N,M))
main()



