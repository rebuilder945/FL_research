def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calcuiate_capital(N,M):
       for x in range(M):
       N=N*1.003
       print(N)
main()



