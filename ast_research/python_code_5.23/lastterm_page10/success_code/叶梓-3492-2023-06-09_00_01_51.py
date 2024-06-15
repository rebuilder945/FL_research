a=input()
lst=[]
for x in a:
    b=a.count(x)
    if b==1:
        lst.append(x)
if len(lst)==0:
    print("None")
else:
    print(lst[0])
