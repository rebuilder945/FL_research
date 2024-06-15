def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
       def calculate_capital(N,M):
           i=0
           while i<M:
               N+=N*0.003
               i+=1
           return N
       print('%.4f'%(calculate_capital(N,M)))
main()



