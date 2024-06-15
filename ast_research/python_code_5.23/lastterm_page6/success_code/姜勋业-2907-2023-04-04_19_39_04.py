def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(a,b):
      k=1.003**b*a
      print("%.4f"%(k))
main()



