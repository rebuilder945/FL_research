def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(x,y):
    x=1.003**y*x
    print('%.4f'%x)
main()



