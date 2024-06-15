def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
       fBalance=N
       fRate=0.003
       for i in range(M+1):
            fBalance=fBalance+fBalance*fRate
main()



