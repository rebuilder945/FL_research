def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
        N = (N+N*0.003)**M
        print(N)
main()



