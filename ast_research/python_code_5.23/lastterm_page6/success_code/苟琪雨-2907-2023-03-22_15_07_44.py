def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def  calculate_capital(N,M):
    n=1
    while n<=M:
        N=N+N*0.003
        n=n+1
    print("%.4f"%N)

main()



