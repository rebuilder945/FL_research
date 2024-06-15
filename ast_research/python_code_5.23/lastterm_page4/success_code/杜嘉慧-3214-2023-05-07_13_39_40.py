lst=eval(input())
new=[]
a=lst.count(0)
for i in lst:
    if i!=0:
        new.append(i)
new+=[0]*a
print(new)
