x=str(input())
a=[]
for i in x:
    if x.count(i)<2:
        a.append(i)
if len(a)>0:
    print(a[0])
else:
    print("None")


