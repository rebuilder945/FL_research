def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
       for i in range(M):
             c=N+N*0.003
             print("%.4f"%c)
main()



