def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    money=M*pow(1.003,N)
    print('%.4f'%money)
main()



