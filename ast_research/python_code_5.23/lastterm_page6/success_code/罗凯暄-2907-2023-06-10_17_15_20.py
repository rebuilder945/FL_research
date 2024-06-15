def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculat_capital(N,M):
     r = 0.003
     F = N*(1+r)**N
     print("%.4f"% F)
def main():
     N,M = map(int,input().split())
     calculate_capital(N,M)
main()



