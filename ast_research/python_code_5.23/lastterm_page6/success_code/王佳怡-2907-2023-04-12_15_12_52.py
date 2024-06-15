def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def  calculate_capital(N,M):
    a=N*(1+3/1000)**M
    print("%.4f" %(a))
main()



