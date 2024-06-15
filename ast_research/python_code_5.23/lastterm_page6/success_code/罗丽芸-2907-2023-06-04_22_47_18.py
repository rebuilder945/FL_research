def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(n,m):
    s=n*1.003**m
    print('%.4f'%s)
main()



