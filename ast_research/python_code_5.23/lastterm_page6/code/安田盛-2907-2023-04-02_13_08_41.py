def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)

        print("%.4f"%(calculate_capital(N,M)))
def calculate_capital(N,M):
    x=N*(1+0.003)**M
    return x

main()



