def main():
    num = eval(input())
    calculate_e(num)
def F(n):
        if n==0:
                return 1
        else:
           return n*F(n-1)
def calculate_e(n):
      b=[]
      for i in range(0,n+1):
             y=1/F(i)
             b.append(y)
      c=sum(b)
      print("%.6f" %c)
main()


