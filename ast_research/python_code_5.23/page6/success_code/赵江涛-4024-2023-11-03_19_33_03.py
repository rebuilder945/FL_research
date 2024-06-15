def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
      r = 0
      s = 0
      while a> r:
           s = a*10**r+s+a
           r+=1
      s = s-a 
      print(s)
main()

