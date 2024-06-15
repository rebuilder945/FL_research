s=input()
ans=input()
lst=[]
for x in s:
    if x!=ans:
        lst.append(x)
    else:
        lst.append(" ")
print("".join(x for x in lst))
