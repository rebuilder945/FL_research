def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(k):
      s=0
      d=0
      for i in range(0,k):
            s=s+10**i*k
            d=d+s
      print(d)
main()

