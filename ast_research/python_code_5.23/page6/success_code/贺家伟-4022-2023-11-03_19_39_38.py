def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    for i in range(0,M+1):
        N=N+N*3/1000
    return N
main()



