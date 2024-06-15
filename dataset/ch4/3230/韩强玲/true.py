a = eval(input())
a.sort(reverse = True)
b =''
if sum(a)==0:
  print("0")
else:
  for i in a :
   b = b+str(i)
print(b)

