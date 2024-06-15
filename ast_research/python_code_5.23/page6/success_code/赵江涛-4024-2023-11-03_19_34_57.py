def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
      r = 0
      s = 0
      b = a
      while a> r:
           s = b*a*10**r+s
           r+=1
           b-=1
      print(s)
main()

