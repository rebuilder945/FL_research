def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
       for year in range(1,M+1,1):
       m = N*(1+0.003)**year
       print(m)

main()



