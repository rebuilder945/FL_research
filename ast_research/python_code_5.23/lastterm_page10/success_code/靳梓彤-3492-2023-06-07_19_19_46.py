string=input()
lst=[]
for i in string:
    if string.count(i)==1:
        lst.append(i)
print(lst[0])
if len(string)==0:
    print("None")
else:
    for i in string:
        if string.count(i)==1:
            lst.append(i)
    print(lst[0])
