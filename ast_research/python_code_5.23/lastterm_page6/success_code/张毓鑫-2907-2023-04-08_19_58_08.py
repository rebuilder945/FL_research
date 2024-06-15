def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
        while M>0:
            N=N*1.003
            M-=1
            calculate_capital(N,M)
        else:
            print('%.2f',N)
main()



