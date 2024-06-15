def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
        for i in range(M+1):
            lrun=N*0.003
            i+=1
            N=N+lrun
        print(N)  
       
main()



