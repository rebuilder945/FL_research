def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
        print("%.4f"%calculate_capital(N,M))
        
def calculate_capital(N,M):
        for i in range(1,M+1,1):
            N=N+N*0.003
        return N
main()



