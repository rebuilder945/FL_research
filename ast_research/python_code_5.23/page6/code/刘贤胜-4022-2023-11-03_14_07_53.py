def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    for x in range(N):
    M=M+M*0.005
    print("%.2f"%(M))
main()



