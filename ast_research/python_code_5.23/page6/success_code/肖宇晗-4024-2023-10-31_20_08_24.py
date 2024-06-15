def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
      b = str(a)
      sum = 0
      for i in range(a):
            c=int(b*(i+1))
            sum+=c
      print(sum)
main()

