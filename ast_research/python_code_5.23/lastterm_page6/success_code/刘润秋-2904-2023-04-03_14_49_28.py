def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
      s=0
      m=0
      n=a
      if a<10:
         while m<a+1:
               s+=m*a*10**n
               m+=1
               n-=1
         print(s)
      else:
         while m<a+1:
               s+=m*a*10**(2*n)
               m+=1
               n-=1
         print(s)
main()

