def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    print("%.4f"%calculate_capital(N,M))
def calculate_capital(N,M):
    N=N*(1003/1000)**M
    return N
main()



