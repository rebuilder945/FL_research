def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
   sums=0
   b=[]
   for i in range(1,a+1):
      sums=sums+a
      a=a*10+a
      b.append(sums)
      print(max(sums))
main()

