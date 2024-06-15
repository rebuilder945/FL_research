def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(x,y):
    q=x*(1+0.003)**y
    print("%.4f"%q)
main()



