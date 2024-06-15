def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    flixi=N*(1.003)**M
    print(flixi)
main()



