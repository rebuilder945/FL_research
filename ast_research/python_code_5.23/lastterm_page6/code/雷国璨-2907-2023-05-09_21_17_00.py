def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    p=N*(1+0.008)**M
    print(p%.4f)
main()



