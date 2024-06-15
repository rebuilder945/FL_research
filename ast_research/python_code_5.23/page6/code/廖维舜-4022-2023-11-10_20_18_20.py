def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
       T=N*(1.003**M)
       Print('%.4f'%(T))
       return T
main()



