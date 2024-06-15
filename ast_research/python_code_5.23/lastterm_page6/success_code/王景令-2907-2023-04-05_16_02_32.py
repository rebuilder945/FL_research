def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    a = (N + 0.003*N)**M
    print("%.4f"%(a))
main()



