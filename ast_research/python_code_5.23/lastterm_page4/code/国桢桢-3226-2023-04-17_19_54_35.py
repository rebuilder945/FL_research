def search(a):
 b = []
 c = []
 e = []
 k = []
 for x in a:
  if x not in b:
   b.append(x)
   for i in range (len(b)):
    d = a.count(b[i])
   if d >len(a)//2:
    e.append(b[i])
     if len(e)==0:
      return"False"
     else:
      return e[0]






nums = eval(input())
y = search(nums)
print(y)


