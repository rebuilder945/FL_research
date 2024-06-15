def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
   lst = []
   for x in range(a):
      b = str(a)*x
      lst.append(b)
   lst1 = map(int,lst)
   c = sum(lst1)
   print(c)
main()

