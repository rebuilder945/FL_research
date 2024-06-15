def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
        k=1.003**M*N
        print("%.2f"%(k))
main()



