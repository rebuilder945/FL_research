def main():
    num = eval(input())
    calculate_e(num)
import math
def calculate_e(a):
  e=1
  for i in range(a):
    e=e+1/math.factorial(i)
  print(e)
  
main()


