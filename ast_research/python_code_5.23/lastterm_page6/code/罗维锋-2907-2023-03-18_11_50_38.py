def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def  calculate_capital(n,m):
        for x in range(m):
            s=n*0.003
            n+=s
        print("{:.4f}"format(n))
main()



