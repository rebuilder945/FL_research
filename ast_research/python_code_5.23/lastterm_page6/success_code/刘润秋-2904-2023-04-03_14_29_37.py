def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
      s=0
      m=0
      n=a
      while m<10**a:
               s+=m
               m+=a*10**n
               n-=1
main()

