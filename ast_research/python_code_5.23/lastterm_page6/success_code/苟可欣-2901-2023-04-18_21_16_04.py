x=0
lst=[]
while x != "#":
    x=input()
    lst.append(x)
a=lst.pop()
b=len(lst)
lst1=[]
for i in lst:
    c=eval(i)
    lst1.append(c)
k=sum(lst1)
print(b,k)
