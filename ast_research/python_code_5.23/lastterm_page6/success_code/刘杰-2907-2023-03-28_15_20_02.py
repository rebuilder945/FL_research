def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(x,y):
    while y>0:
        x=x*1.003
        y-=1
    print('%.4f'%x)

main()



