def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    c=1.003**M
    return('%.4f'%N*c)
main()



