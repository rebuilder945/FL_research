def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
       def calculate_capital(x,y):
              for i in range(1,M):
                   N=(N*0.003+N)*N*i

             

main()



