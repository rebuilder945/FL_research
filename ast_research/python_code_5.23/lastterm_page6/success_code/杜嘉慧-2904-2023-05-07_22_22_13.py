def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
      c=str(a)
      s=0
      for i in range(a):
           s+=int(c*(i+1))
      print(s)
main()

