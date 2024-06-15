def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def  calculate_capital(N,M):
      for x in range(1,M+1,1):
                 N*=1.003
      print("%.4f"%N)
      
main()



