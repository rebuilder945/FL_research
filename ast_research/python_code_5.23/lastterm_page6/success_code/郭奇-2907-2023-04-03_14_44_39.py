def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    for i in M:
        a = N **i
    b = "%.4f"%a
main()



