def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
   sum=0
   n=a
   tmp=a
   for i in range(1,n+1):
      sum=sum+a
      a=a*10+tmp
print(sum)

main()

