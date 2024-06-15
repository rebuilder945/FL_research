def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
      b=str(a)
      d=0
      for x in range(a):
            c=b+b*x
            c=int(c)
            d=d+c
      print(d)
main()

