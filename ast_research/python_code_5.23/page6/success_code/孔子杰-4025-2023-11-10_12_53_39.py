def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
      from math import factorial as f
      
      sum1=1
      for i in range(1,n+1):
            sum1=sum1+1/(f(i))
      print("%.6f"%(sum1))
      
main()


