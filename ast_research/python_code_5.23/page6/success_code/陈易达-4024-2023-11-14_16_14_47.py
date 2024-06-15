def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
  x = a
  ls = []
  while len(ls) < a:
    ls.append(x)
    x = a+x*10
  print(sum(ls))
main()

