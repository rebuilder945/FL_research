def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def  calculate_capital(N,M):
      n=N[1]
      m=M[1]
     ALL=n*1.003**m
     print(ALL)

main()



