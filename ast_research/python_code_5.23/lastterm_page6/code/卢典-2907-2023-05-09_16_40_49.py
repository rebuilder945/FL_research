def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
       N*=1.0003**M
       print("{:.4f}".format(N))        
main()



