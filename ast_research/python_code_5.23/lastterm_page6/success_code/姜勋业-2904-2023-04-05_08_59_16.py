def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(k):
      s=0
      for i in range(k):
            s+=10**i*k
      print(s)
main()

