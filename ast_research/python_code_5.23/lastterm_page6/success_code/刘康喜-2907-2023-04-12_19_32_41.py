def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(a, b):
    c=a*1.003**5
    print('%.4f'%c)
main()



