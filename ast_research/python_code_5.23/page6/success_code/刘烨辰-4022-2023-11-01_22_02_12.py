def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(n,m):
    for i in range(0,m):
        n = 1.003*n
    print("%.4f"%n)
main()



