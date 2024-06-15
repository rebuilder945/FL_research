def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    for i in range(M):
        N=N+0.03*N
        i=i+1
  N1=float(N)
  print("%.4f"%N1)
main()



