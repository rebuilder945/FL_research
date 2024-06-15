def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def  calculate_capital(N,M):
      for x in range(1,M):
                 N+=(N*0.003+N)
      print("%.4f"%N)
      
main()



