def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    for x in range(M):
        a=N*0.003
        N=N+a
    return N
print("%.4f"%(N))
main()



