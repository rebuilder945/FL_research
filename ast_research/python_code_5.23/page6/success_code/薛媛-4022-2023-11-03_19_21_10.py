def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def  calculate_capital(N,M):       
       for x in range(M):
           N=N*1.003
       print("%.4F"%N)
main()



