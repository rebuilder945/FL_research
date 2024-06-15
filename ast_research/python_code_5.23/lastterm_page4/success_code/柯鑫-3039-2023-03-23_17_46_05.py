list1=eval(input())
list1=list(list1)
a=max(list1)
b=min(list1)
c=0
d=0
for x in list1:
    if x==a or x==b:
        list1[d]='e'
        c+=1
    d+=1
while c>0:
    list1.remove('e')
    c-=1
print (list1)
