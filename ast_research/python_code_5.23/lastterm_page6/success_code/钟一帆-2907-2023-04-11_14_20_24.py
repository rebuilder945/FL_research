def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def  calcilate_capital(N, M):
        smoney=N*(1+0.003)**M 
        print(smoney )
main()



