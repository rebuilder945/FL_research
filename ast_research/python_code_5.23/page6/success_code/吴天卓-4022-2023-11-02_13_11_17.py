def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate(N,M):
    
    s=N*(1+0.003)**M
    print(s)
main()



