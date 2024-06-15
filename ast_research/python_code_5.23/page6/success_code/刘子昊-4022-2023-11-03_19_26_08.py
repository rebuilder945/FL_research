def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    rate=0.003
    for i in range(M):
        N+=N*rate
    print(f'{N:4F}')
main()



