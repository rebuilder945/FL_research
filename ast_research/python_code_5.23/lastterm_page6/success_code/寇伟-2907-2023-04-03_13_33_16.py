def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    total=N*1.003**M
    print('%.4f'%total)
main()



