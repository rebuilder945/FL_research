def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    ben=N*((1+0.003)**M)
    print(ben)
main()



