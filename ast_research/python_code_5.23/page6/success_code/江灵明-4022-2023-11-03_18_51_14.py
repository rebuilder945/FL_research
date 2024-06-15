def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    for i in range(M):
        N=N+N*0.03
    print("%.4f"%N)
main()



