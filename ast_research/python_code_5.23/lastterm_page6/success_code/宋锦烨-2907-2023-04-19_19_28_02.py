def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def calculate_capital(a,b):
  for i in range(b-1):
    x=a*0.003
    a=a+x
  print('%.4f' %a)

main()



