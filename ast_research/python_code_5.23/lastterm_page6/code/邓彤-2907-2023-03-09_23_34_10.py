def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
       calculate_capital=N*(（1+0.003)**M)
       a=calculate_capital
       b="%.4f"%a
       print(b)
main()



