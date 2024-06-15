b={}
while True:
    a=input()
    if a=="q":
        break
    else:
        b[a]=b.get(a,0)+1
lst=[]
for k,v in b.items():
    lst.append([k,v])
    lst.sort(key=lambda x:x[1],reverse=True)
lst2=[]
lst2.append(lst[0][0])
lst2.append(lst[0][1])
print(" ".join(map(str,lst2)))



