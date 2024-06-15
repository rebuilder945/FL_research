def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
      s=0
      for i in range(a):
           s=s+a**(i+1)
      print(s)
main()

