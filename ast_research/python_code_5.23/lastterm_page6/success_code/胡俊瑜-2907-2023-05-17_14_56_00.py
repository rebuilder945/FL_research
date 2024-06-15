def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
      i=0.
      while i<M:
               N+=N*(3/1000)
               i=i+1
      s="%.4f"%(N)
      print(s)
main()



