def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    c=n*(1.003**M)
    print("%.2f"%(c))
main()



