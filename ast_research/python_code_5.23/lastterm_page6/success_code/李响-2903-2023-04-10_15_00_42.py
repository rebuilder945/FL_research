def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
   s = 1
   m = 1
   x = 0
   while s <= num:
      x = x + m
      s = s +1
      m = m*(1/s)
   print('%.6f'%(num))

      
      
main()


