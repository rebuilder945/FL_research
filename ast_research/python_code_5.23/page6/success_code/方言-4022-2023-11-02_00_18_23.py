def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital():
  for i in range(M):
    N=N*3/1000+N
  print("%.2f"%(N))
    
main()



