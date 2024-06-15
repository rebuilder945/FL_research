def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    q=N*(1+0.0003)**M
    print("%.4f"%q)
main()



