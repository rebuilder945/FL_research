s=input()
print(s)
ls=[]
for x in s:
    ls.append(x)
for x in range(len(ls)):
    if chr(ls[x])<=chr("Z") and chr(ls[x])>=chr("A"):
        ls[x]=ord(che("Z")-chr(ls[x])+1)
    if chr(ls[x])<=chr("z") and chr(ls[x])>=chr("a"):
        ls[x]=ord(che("z")-chr(ls[x])+1)
print(*ls)
