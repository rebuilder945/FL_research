def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
        N,M  =  map(int,input().split())
        Q=N*(1.003**M)
        print("%.4f"%(Q))
main()



