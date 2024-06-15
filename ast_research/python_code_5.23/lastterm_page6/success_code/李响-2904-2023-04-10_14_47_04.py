def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
   m = 1
   s = 1
   c  = a   
   while m <= a:
      s = m*10**c
      m = m +1
      c = c -1
   print(int(a*s))
      
main()

