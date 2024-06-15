def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    a = N*(1.003**M)
    print("%.4f"%(a))
main()



