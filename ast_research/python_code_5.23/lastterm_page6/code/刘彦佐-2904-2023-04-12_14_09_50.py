def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
      s=0
      for i in range(a,a+1):
           j=str(a)*i
          s=s+int(j)
      print(s)
main()

