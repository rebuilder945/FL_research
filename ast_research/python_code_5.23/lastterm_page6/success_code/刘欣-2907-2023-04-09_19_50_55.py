def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    x=0
    while x<=M:
        N=N*(M+1)
        x+=1
    print("%.4f"%(N))
main()



