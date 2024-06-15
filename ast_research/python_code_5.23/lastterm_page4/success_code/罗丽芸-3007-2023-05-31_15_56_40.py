i=eval(input())
h=[]
n,m=eval(input())
n1=max(n,m)
n2=n1+1
m2=m+1
if n1>(len(i)-1) :
  print('error')
elif n<=m:
  for x in range(len(i)) :
    if x not in list(range(n,m)):
          h.append(i[x])
  print(h)
else:
    for x in range(len(i)) :
      if x not in list(range(m2,n2)):
          h.append(i[x])
    print(h)


