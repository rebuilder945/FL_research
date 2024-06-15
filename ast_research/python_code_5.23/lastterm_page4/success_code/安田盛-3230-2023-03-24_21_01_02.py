lst=eval(input())
lst.sort(reverse=True)
a=[]
for i in lst:
    b=str(i)
    a.append(b)
y=a[0]
for x in a[1:]:
    y=y+x
print(int(y))

    

