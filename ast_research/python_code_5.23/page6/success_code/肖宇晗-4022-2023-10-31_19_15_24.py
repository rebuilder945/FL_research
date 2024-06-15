def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
       for i in range(M):
             raN = N*0.003
             N = N+raN
       return print("%.4f"%(N))
         
main()



