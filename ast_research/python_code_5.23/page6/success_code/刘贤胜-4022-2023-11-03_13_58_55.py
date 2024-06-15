def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    a=(M*3/1000)**N
    print(a)

main()



