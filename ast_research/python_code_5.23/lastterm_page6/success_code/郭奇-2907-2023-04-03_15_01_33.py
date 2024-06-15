def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
a = N
for i in M:
    a = a *0.003 + a
capital = "%.4f"%a

main()



