def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
      from math import factorial as f
      n=num
      sum1=1
      for i in range(1,n):
            sum1=sum1+1/(f(i))
      print("%.6f"%sum1)
      
main()


