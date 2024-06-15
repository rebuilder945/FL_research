def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(x,y):
    capital=x*(1+0.003)**y
print("%.4f"%capital)
    
main()



