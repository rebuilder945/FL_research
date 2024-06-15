lst=[]
sums=0
while True:
    s=input()
    if str(s)!="#":
        lst.append(int(s))
    else:
        break

for x in lst:
    sums+=int(x)
print(len(lst),sums)
