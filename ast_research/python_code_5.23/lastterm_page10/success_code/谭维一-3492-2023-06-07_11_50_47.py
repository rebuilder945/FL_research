list=list(input())
if input=="":
    print("None")
l=[]
for i in list:
    n=list.count(i)
    if n==1:
        l.append(i)
print(l[0])

