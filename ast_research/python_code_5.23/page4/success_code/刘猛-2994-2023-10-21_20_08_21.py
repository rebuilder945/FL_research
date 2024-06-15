a = eval(input())
n,m = eval(input())
if n>len(a) or -n>len(a):
    print("error")
else:
  c = int(a[n])
  a.remove(a[n])
  for i in range(m):
     a.append(c)
  print(a)

