def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(n,m):
    n=n*1.003**m
    print("%.4f"%(n))
main()



