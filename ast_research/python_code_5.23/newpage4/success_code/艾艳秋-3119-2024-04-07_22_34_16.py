list1=eval(input())
new=[]
for i in list1:
    if i not in new:
        new.append(i)
print(new)

