def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(a,b):
      k=1.003**a*b
      print("%.2f"%(k))
main()



