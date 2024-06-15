def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    main = N*(1.0003)**M
    print(%4.f %(main))
main()



