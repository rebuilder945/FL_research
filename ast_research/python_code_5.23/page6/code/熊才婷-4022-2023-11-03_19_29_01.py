def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
        def Money(N,M):
            for i in range(M):
                N+=N*0.003
            return N
        x=Money(N,M)
        print("%.4f"%x)
main()



