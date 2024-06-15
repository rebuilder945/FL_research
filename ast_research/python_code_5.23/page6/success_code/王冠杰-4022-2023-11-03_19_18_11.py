def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M) :
    h=N*(1.003)**M
    print("%.4f"%h)    
main()



