def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    print(“%.4f"%(N*(1.003)**M))
main()



