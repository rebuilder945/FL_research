a=eval(input())
b=[]
for i in a:
    if a.count(i)==1:
     b.append(i)
if len(b)>0:
  b.sort()
  b=','.join(str(x) for x in b )
  print(b)       
else:
    print("False")


