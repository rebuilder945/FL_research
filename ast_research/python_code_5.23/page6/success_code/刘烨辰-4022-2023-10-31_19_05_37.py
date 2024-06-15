def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    for i in range(0,M):
        N = 1.003*N
    print("%.4f"%N)
main()



