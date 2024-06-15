def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
        for x in range(1,M+1):
            ben=N*((1+0.003)**x)
        print(ben)
main()



