def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calulate_capital(N,M):
    for i in range(1,M+1):
        N=N + (N+3/1000)
    print['{:.4f}'.format(N)]
main()



