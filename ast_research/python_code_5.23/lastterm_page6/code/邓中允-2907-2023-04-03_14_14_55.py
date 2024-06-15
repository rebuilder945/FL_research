def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
        q=(N+N*0.0003)**M
        print("%.4f"%q)
main()



