def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
        for i in range(M+1):
                P=N+N*0.003
                print("%.4f"%(P))
main()



