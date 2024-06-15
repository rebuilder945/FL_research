def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    w=N*(1003/1000)**M
    print("%.4f"%w)
main()



