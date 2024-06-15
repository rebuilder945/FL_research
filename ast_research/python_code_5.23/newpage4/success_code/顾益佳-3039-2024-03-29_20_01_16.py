s = list(eval(input()))
max = max(s)
min = min(s)
n1 = s.count(max)
n2 = s.count(min)
if n1 == 1:
    s.remove(max)
else:
   for x in range(1,n1+1):
     s.remove(max)
if n2 == 1:
    s.remove(min)
else:
   for x in range(1,n2+1):
     s.remove(min)
print(s)

