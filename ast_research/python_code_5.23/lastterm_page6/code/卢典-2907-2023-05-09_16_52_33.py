def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
       for i in M:
       N=N+N*0.003
       print("%.4f"%N)  
main()



