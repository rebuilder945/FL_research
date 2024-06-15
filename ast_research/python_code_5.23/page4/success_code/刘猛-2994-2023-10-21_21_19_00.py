a = list(input().split(","))
b = []
n,m = eval(input())
if n>len(a) or -n>len(a):
    print("error")
else:
  c = int(a[n])
  for i in range(m):
     a.append(c)
  for x in a[0:]:
     b.append(int(x))
  print(b)

