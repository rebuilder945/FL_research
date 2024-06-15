def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    n=N*(1+0.003)**M
    print("%.4f"%n)
main()



