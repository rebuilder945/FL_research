def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(N,M):
       a = N*(1+0.003)**(M-1)
       prant(a)
               
main()



