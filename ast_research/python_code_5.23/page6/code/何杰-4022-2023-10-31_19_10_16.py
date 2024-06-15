def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
         for  i in rang(1,M+1):
               N=N+ N*0.003
         print(‘%.4f'%N)
main()



