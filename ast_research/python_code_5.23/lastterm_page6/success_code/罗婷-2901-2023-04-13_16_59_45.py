lst=[]
sum=0
i=input()
while i!='#':
    lst.append(i)
    i=input()
for x in lst:
    x=int(x)
    sum+=x
print(len(lst),sum)


