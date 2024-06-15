def main():
    N,M = map(int,input().split())
    calculate_capital(N,M)
def  calculate_capital(x,y):
      jishu=x
      while y>0:
            jishu=jishu+jishu*0.003
            y-=1
      print("%.4f"%jishu)
main()



