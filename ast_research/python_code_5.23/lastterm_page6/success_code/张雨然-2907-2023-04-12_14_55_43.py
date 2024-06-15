def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
 i=N*(1+0.03)**M
 print('%.4f'%i)

main()



