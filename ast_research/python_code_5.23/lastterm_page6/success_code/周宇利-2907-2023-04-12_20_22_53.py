def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
b=0.003
for i in range(M+1):
     N=N+N*b
main()



