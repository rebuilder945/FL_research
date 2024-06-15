def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    x=0
    while x<=M:
        x+=1
        N=N+N*0.003
    print('%.4f'%(N))
main()



