l=input()
ls=[]
l1=[]
l2=[]
while l !="ok":
    ls.append(l.split())
    l = input()
else:
    pass
a = len(ls)
for x in range(a):
    l1.append(ls[x][0])
    l2.append(int(ls[x][1]))
print(sorted(l1))
print(sorted(l2))
if "India" in l1:
    print("yes")
else:
    print("no")
print(sum(l2))
