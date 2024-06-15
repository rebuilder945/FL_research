def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(x,y):
 while y>0 :
  x=x*0.003+x
  y=y-1
else: print("%.4f"%x)
main()



