def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):        
    for i in range(M):
        N = N+(N*3/1000)
    print("%.4f"%N)
            
main()



