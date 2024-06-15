def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(k):
      s=0
      for i in range(0,k-1):
            s+=10**i*k
      print(s)
main()

