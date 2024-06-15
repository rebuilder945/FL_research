lst=eval(input())
newlist=lst[::-1]
new=[]
for i in newlist:
    if i not in new:
        new.append(i)
print(new[::-1])
