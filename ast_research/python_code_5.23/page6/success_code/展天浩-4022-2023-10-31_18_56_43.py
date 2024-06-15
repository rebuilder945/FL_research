def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    def calculate_capital(N,M):
        for i in range(M):
            N=N+N*0.003
print(N)
main()



