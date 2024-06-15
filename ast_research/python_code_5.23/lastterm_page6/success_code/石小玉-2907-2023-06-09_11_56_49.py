def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
        i=0
        while M>i:
                N=N+N*0.003
                i=i+1
        print("%.4f"%(N))
main()



