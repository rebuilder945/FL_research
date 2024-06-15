
a = eval(input())
if a == []:
  print([])
else:
    m = max(a)
    n = min(a)
    maxi = a.count(m)
    minn = a.count(n) 
    for i in range(maxi):
         a.remove(m)
    for i in range(minn):
         a.remove(n)
print(a)

