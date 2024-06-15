a = eval(input())
b = []
d = {}
while a != q:
  b.append(a)
  a = eval(input())
for i in b:
 d[i] = b.count(i)
for k in d:
 f = list(d[k])
if d[k] is max(f):
 print(k,d[k])
 

     
