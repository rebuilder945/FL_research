def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate capital(n,m):
     print(f'{calculate(n,m):4f}')
def calculate(n,m):
    if m==():return n
    else:return calculate(n*1.003,m-1)
main()



