def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
        for i in range(M):
                n=N*0.003
                N=N+n
        print('%.4f'%(N))
main()



