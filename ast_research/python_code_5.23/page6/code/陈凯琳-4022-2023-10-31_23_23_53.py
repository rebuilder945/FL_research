def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
       calculate_capital=(N+N*0.003)**M
       print("%.4f"%calculate_capital)
        
main()



