def main():
    num = eval(input())
    calculate_e(num)
import math
def calculate_e(num):
      e=1
      for x in range(1,num+1):
           e=e+1/(math.factorial(x))
      print("%.6f"%(e))

      
           
main()


