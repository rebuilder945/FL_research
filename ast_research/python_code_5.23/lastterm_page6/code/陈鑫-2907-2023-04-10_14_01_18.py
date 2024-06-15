def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    def calculate_capital(a,b):
        for i in range(b):
        a=a*(1+3/1000)
        c=("%.4f"%(a))
        print(c)
    calculate_capital(10000,5)

main()



