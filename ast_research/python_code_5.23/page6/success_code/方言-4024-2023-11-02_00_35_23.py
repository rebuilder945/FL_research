def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
  cs=csi=1
  for j in range(a-1):
    cs=cs*10+1
    csi+=cs
  sum=csi*a
  print(sum)
  
main()

