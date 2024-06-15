def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    N = ((1 + 0.003)**M)*N
    print("%.4f"%(N))
main()



