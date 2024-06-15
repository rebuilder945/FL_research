def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
 l = []
 for i in range(1,a+1):
  b = int(str(a)*i)
  l.append(b)
  c = sum(l)
 print(c)
main()

