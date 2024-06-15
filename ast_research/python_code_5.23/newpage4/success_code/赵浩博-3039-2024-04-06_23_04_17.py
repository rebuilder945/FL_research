l=eval(input())
l1=l.copy()
for i in l:
    if i==min(l):
       l1.remove(i)
    elif i==max(l):
         l1.remove(i)
print(l1)
