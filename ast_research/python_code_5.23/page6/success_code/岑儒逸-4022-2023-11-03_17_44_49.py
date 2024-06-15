def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    m=0
    while m<M:
        N=N*(1.003)
        m+=1
print("%.2f"%N)
main()



