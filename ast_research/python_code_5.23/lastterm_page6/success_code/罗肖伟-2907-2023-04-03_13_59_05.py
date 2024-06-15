def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(x,y):
             for i in range(y):
               x=x*1.003
             print("%.4f"%(x))

main()



