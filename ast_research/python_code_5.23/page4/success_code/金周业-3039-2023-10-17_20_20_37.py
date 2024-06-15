list1=eval(input())
a=max(list1)
b=min(list1)
c=0
d=0
for i in list1:
    if i == a:
        c=c+1
for j in range(c):
    list1.remove(a)

for i in list1:
    if i == b:
        d=d+1
for j in range(d):
    list1.remove(b)
print(list1)

