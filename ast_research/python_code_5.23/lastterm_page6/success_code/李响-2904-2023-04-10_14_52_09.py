def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
   m = 0
   s = 0
   c  = a   
   while s < a:
      m = c*10**s + m
      s = s +1
      c = c -1
   print(int(a*m))
      
main()

