def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
   s = 1
   m = 1
   x = 1
   while s <= num:
      m = m*(1/s)
      x = x + m
      s = s +1
   print('%.6f'%(x))

      
      
main()


