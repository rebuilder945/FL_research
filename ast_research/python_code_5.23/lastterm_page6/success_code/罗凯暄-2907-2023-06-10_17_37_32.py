def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
     r = 0.003
     F = N*(1+r)**M
     print("%.4f"% F)

main()



