def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
      k=0
      n=0
      m=a
      while n<a:
          k+=a*10**n
          n+=1
          m-=1
          s+=k
      print(s)
main()

