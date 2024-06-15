a=eval(input())
num=0
k=[]
for i in range(len(a)):
    b=a[i]
    if b==0:
     num+=1
    else:
     k.append(b)
for x in range(num):
  k.append(0)
print(k)
     



