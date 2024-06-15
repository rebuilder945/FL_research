def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    for i in range(M+1):
        M=M+1
        N=N*((1+0.003) ** M)
    return "%.4f"%(M)
main()



