def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
for i in M:
    N = N *0.003 + N
capital = "%.4f"%N
return capital
main()



