def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
    def calculate_capital(x,y):
        while y>=10000:
            x=x+x*0.003
    print(x)
main()



