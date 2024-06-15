def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
    for x in M:
        N=N+N*0.003
        s="%.4f" % (N)
        print(s)
    


    
main()



