def main():
    a=int(input())
    calculate_sum(a)
n=0
m=1
while a>0:
  n=n+m*10**(a-1)
  a=a-1
  m=m+1
print(n)
main()

