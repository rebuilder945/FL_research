def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    c=N*(1+0.003)**M
    return('%.4f'%c)
main()



