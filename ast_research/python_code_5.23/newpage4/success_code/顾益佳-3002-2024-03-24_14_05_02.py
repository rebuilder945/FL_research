s = eval(input())
m = list (s)
n = sum(m)/len(m)
if sum(m)%len(m) == 0:
  n = int (n)
  print(n)
else:
  t = "%.2f" %(n)
  print(t)
   

