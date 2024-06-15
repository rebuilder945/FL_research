def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
     def calculate_capital(N,M):
        for i in range(M):
        D=N*0.003
        N+=D
    print('%.4f'%N)
main()



