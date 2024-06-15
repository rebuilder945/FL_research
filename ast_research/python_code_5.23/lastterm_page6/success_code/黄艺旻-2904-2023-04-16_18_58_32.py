def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
   sum=0
   for i in range(1,a+1):
      sum=sum+a
      a=a*10+a
print(sum)

main()

