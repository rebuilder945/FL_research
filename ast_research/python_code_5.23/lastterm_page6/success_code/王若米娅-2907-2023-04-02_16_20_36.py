def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)

    print("%.4f"%(calculate_capital(N,M)))
def calculate_capital(N,M):
    b=N
    for i in range(M):
        c=b*3/1000
        b+=c
    return b
main()



