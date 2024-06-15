def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    N1 = N*1.003**(M-1)
    print('%.2f'%N1)
main()



