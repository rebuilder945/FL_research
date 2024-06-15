def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
  s = 0
  b = a
  for i in range(1,a+1):
    s =  s + b
    b = b + b*10**i
  print(s)
main()

