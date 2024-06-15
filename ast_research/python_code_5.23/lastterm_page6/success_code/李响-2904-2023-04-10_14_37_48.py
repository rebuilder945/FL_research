def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
   m = a
   c  = a   
   while m >= 0:
      a = a*10**(m-1)
      m = m -1
   print(c*a)
      
main()

