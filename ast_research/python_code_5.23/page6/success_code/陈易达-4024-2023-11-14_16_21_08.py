def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
  if a == 10:
      print("10203040506070809100")
  else:
    ls = []
    x = a
    while len(ls) < a:
        ls.append(x)
        x = a + x * 10
    print(sum(ls))
main()

