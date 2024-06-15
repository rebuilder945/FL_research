def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(n,m):
    t=1+3/1000
    tt=m(t)**n
    print("{:.4f}".format(tt))
main()



