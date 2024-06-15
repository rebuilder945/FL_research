def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
N>=1000
F = N*(1+(3/1000))**M
print("%.4f"%(F))
main()



