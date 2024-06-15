def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(n,m):
    a=n*pow(1.0003,m)
    print(a)
main()



