def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
  i=1;sum=a;cs=1
  while i!=a:
    sum=sum*cs
    cs=cs*10+1
  print(sum)
  
main()

