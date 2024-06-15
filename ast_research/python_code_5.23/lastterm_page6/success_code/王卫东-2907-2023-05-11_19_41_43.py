def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(x,y):
    while y>0: 
        x=x+x*0.003
        y = y-1
    print("%4.f"%x) 
main()



