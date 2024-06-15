def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
i=N*1.003**M
print('%.4f'%i)
main()



