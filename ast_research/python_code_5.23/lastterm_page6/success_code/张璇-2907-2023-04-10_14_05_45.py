def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    for x in range(M):
        mon=N*1.003
        N=mon
    print("%.4f"%(mon))
main()



