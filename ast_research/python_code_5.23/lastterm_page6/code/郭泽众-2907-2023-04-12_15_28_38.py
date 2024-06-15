def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
   print(calculate_capital(N,M) == (N*(1.003))**M)
main()



