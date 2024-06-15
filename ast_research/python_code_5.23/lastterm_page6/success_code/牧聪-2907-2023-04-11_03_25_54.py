def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N, M):
    for _ in range(M):
        N += N * 0.003
    print(round(N, 4))
main()



