def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
F = N*(1+(3/1000))**M
print(%.4f%(F))
main()



