def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(a,b):
    c=1.003**b
    return('%.4f'%a*c)
main()



