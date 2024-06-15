def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
      n = 0
      while n < M:
           N = N*0.003 + N
           n = n + 1
      print(N)     
main()



