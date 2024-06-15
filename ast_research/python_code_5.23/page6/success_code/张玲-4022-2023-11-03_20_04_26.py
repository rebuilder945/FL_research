def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N, M):
    interest_rate = 0.003
    for _ in range(M):
        N += N * interest_rate 
    print('{:.4f}'.format(N)) 
main()



