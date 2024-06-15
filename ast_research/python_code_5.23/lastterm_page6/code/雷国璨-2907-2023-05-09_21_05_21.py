def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    N=N*((1+0.008)**M)
    return N%.4f
main()



