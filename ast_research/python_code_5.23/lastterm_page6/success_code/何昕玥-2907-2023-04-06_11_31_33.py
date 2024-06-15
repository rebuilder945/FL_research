def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    for i in range(M):
        N=N+0.003*N
        i=i+1
        X=float(N)
    print("%.4f"&X)
main()



