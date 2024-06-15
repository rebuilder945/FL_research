a = list(eval(input()))
b = []
for i in a:
   b.append(i)
   for x in b:
      b.count(x)
      if x != 1:
         b.remove(x)

print(b)

