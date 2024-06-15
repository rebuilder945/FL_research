def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(n,m):
    sums = n
    for i in range(1,m+1):
        sums = sums + sums*0.003
    print("%.4f"%(sums))

main()



