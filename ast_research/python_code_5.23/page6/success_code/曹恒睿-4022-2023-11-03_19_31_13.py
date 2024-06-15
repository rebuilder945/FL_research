def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(n,m):
  for i in range(m):
    n = n*1.003
  print("%.4f"%(n))
main()



