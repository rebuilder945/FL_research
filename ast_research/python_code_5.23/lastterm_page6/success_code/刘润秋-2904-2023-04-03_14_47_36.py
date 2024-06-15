def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
      s=0
      m=0
      n=a
      while m<a:
               s+=m*a*10**n
               m+=1
               n-=1
      print(s)
main()

