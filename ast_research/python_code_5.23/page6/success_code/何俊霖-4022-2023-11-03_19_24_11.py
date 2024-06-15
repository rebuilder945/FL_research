def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
        sum=float(N)
        for i in range(0,M):
            sum = float(sum*1.003)
        print("%.4f"%(sum))
main()



