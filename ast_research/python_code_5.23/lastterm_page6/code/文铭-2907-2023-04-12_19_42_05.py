def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_ capital(a,b):
       for i in range(b):
             a += a*0.003
       print( "%.4f"%a)
    
main()



