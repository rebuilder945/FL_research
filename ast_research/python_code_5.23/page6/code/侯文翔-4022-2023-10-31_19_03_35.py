def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
      a=[]
      for i in range(M):
            N=N+N*0.001
      print("%.2f"%N)
main()



