def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    for i in range(1,M+1):
        N=N*(1+0.003)
    print("%.4f"%N) 
main()


