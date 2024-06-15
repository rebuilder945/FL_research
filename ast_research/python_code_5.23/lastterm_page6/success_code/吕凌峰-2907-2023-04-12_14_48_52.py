def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def  calculate_capital(N,M):
            for x in range(0,M):
                N=N*1.003**(x+1)
            print("%.4f"%N)
    
main()



