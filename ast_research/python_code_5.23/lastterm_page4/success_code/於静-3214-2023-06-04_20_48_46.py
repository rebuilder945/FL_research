lst=eval(input())
x=lst.count(0)
new=[]
for i in lst:
    if i!=0:
        new.append(i)
for i in range(x):
    new.append(0)
print(new)
