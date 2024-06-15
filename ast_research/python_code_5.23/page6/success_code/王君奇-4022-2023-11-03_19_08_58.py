def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
N=N*(1.003**(M-1))
print("%.4f"%N)

main()



