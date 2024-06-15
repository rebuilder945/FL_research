def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    total=N
    for i in range(1,M+1):
        total=total*1.003
    print("%.4f"%total)
main()



